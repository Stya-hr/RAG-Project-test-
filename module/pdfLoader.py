import re

import fitz
from tqdm import tqdm
from treelib import Tree
import json


class pdfReader():
    """pdf处理器"""

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.pdf = fitz.open(file_path)
        self.toc = self.pdf.get_toc()
        self.max_level = max([entry[0] for entry in self.toc])
        self.id = [0 for i in range(self.max_level)]

    def tree_spliter(self) -> Tree:
        """生成pdf多叉树"""
        chapter_tree = Tree()
        err_count = 0
        chapter_tree.create_node(
            tag=self.file_path, identifier="root", data=self.file_path
        )
        loading_bar = tqdm(range(len(self.toc)), position=0, desc="pdf loading...")
        for i in range(len(self.toc)):
            level = self.toc[i][0]
            id_title = self.toc[i][1]
            id = self.__get_id__(level)
            id_parent = re.sub(r"[.]\d*$", "", id)  # 父节点id
            # 去除标题中的序号
            title = re.sub(r'^\d([.]\d*)*[^\u4E00-\u9FA5A-Za-z]*','',id_title)
            if level == 1:  # 初级标题
                chapter_tree.create_node(
                    tag=title, identifier=id, parent="root", data=title
                )
            elif level == self.max_level:
                page_index = [self.toc[i][2], self.toc[i + 1][2]]
                pages = self.pdf.pages(page_index[0], page_index[1])
                chapter = ""
                for page in pages:
                    width, height = page.rect.width, page.rect.height
                    # 计算页眉的区域（这里假设页眉在页面的顶部 10%）
                    header_height = height * 0.1
                    header_rect = fitz.Rect(0, 0, width, header_height)
                    main_rect = fitz.Rect(0, header_height, width, height)
                    # 提取主要区域的文本
                    text = page.get_text("text", clip=main_rect)
                    text = text.replace("\n", " ")
                    chapter += "".join(x for x in text if x.isprintable())
                # 段落精准切块
                title_1 = re.sub(r'^\d([.]\d*)*[^\u4E00-\u9FA5A-Za-z]*','',self.toc[i+1][1])
                chapter_plain = re.match("(?<={}).*(?={})".format(title,title_1), chapter)
                if chapter_plain:
                    chapter = chapter_plain.group(0)
                    # print("{}:{}".format(title,title_1))
                else: 
                    chapter_plain = re.match(".*?(?={})".format(title_1), chapter)
                    if chapter_plain:
                        chapter = chapter_plain.group(0)
                        # print("*{}:{}".format(title,title_1))
                    else:
                        chapter_plain = re.match("(?<={}).*".format(title), chapter)
                        if chapter_plain:
                            chapter = chapter_plain.group(0)
                            # print("{}:*{}".format(title,title_1))
                        else:
                            err_count += 1
                chapter_tree.create_node(
                    tag=title, identifier=id, parent=id_parent, data=chapter
                )
            else:
                chapter_tree.create_node(
                    tag=title, identifier=id, parent=id_parent, data=title
                )
            loading_bar.update(1)
        print("missing:", str((err_count/len(self.toc))*100),"%")
        return chapter_tree

    def __get_id__(self, level: int) -> str:
        """获取当前树节点id"""
        self.id[level - 1] += 1  # 注意index-level对应关系
        id = str(self.id[0])
        if level != 1:  # 计算id
            for i in range(1, level):
                id = id + "." + str(self.id[i])
        if level != self.max_level:  # 清除次级节点id
            for i in range(level + 1, self.max_level):
                self.id[i] = 0
        return id

    def from_json(file_path: str) -> Tree:
        """从json文件加载多叉树"""
        with open(file_path, "r") as f:
            data = json.load(f)
            f.close()
        tree = Tree.from_map(child_parent_dict=data)
        return tree


if __name__ == "__main__":
    pdf = pdfReader(
        "document/Digital Image Processing (Rafael C. Gonzalez, Richard E. Woods) (Z-Library).pdf"
    )
    tree = pdf.tree_spliter()
    tree_dict = tree.to_dict(with_data=True, sort=False)
    with open("out.json", "w+") as f:
        formatted_json = json.dumps(tree_dict)
        f.write(formatted_json)
        f.close()
