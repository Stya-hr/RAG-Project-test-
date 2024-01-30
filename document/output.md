

<p>Digital Image
Processing
Third Edition
Rafael C. Gonzalez
University of Tennessee
Richard E. Woods
MedData Interactive
Upper Saddle River, NJ 07458</p>

<p>Library of Congress Cataloging-in-Publication Data on File
Vice President and Editorial Director,ECS: Marcia J.Horton
Executive Editor: Michael McDonald
Associate Editor: Alice Dworkin
Editorial Assistant: William Opaluch
Managing Editor: Scott Disanno
Production Editor: Rose Kernan
Director of Creative Services: Paul Belfanti
Creative Director: Juan Lopez
Art Director: Heather Scott
Art Editors: Gregory Dulles andThomas Benfatti
Manufacturing Manager: Alexis Heydt-Long
Manufacturing Buyer: Lisa McDowell
Senior Marketing Manager: Tim Galligan
© 2008 by Pearson Education,Inc.
Pearson Prentice Hall
Pearson Education,Inc.
Upper Saddle River,New Jersey 07458
All rights reserved.No part of this book may be reproduced,in any form,or by any means,without
permission in writing from the publisher.
Pearson Prentice Hall®is a trademark of Pearson Education,Inc.
The authors and publisher of this book have used their best efforts in preparing this book.These efforts include
the development,research,and testing of the theories and programs to determine their effectiveness.The authors
and publisher make no warranty of any kind,expressed or implied,with regard to these programs or the
documentation contained in this book.The authors and publisher shall not be liable in any event for incidental or
consequential damages with,or arising out of,the furnishing,performance,or use of these programs.
Printed in the United States of America.
10 9 8 7 6 5 4 3 2 1
ISBN 0-13-168728-x
978-0-13-168728-8
Pearson Education Ltd.,London
Pearson Education Australia Pty.Ltd.,Sydney
Pearson Education Singapore,Pte.,Ltd.
Pearson Education North Asia Ltd.,Hong Kong
Pearson Education Canada,Inc.,Toronto
Pearson Educación de Mexico,S.A.de C.V.
Pearson Education—Japan,Tokyo
Pearson Education Malaysia,Pte.Ltd.
Pearson Education,Inc.,Upper Saddle River,New Jersey</p>

<p>To Samantha
and
To Janice, David, and Jonathan</p>

<p>This page intentionally left blank</p>

<p>Contents
Preface xv
Acknowledgments xix
The Book Web Site xx
About the Authors xxi
1
Introduction 1
1.1 What Is Digital Image Processing? 1
1.2 The Origins of Digital Image Processing 3
1.3 Examples of Fields that Use Digital Image Processing 7
1.3.1 Gamma-Ray Imaging 8
1.3.2 X-Ray Imaging 9
1.3.3 Imaging in the Ultraviolet Band 11
1.3.4 Imaging in the Visible and Infrared Bands 12
1.3.5 Imaging in the Microwave Band 18
1.3.6 Imaging in the Radio Band 20
1.3.7 Examples in which Other Imaging Modalities Are Used 20
1.4 Fundamental Steps in Digital Image Processing 25
1.5 Components of an Image Processing System 28
Summary 31
References and Further Reading 31
2
Digital Image Fundamentals 35
2.1 Elements of Visual Perception 36
2.1.1 Structure of the Human Eye 36
2.1.2 Image Formation in the Eye 38
2.1.3 Brightness Adaptation and Discrimination 39
2.2 Light and the Electromagnetic Spectrum 43
2.3 Image Sensing and Acquisition 46
2.3.1 Image Acquisition Using a Single Sensor 48
2.3.2 Image Acquisition Using Sensor Strips 48
2.3.3 Image Acquisition Using Sensor Arrays 50
2.3.4 ASimple Image Formation Model 50
2.4 Image Sampling and Quantization 52
2.4.1 Basic Concepts in Sampling and Quantization 52
2.4.2 Representing Digital Images 55
2.4.3 Spatial and Intensity Resolution 59
2.4.4 Image Interpolation 65
v</p>

<p>vi ■ Contents
2.5 Some Basic Relationships between Pixels 68
2.5.1 Neighbors of a Pixel 68
2.5.2 Adjacency, Connectivity, Regions, and Boundaries 68
2.5.3 Distance Measures 71
2.6 An Introduction to the Mathematical Tools Used in Digital Image
Processing 72
2.6.1 Array versus Matrix Operations 72
2.6.2 Linear versus Nonlinear Operations 73
2.6.3 Arithmetic Operations 74
2.6.4 Set and Logical Operations 80
2.6.5 Spatial Operations 85
2.6.6 Vector and Matrix Operations 92
2.6.7 Image Transforms 93
2.6.8 Probabilistic Methods 96
Summary 98
References and Further Reading 98
Problems 99
3
Intensity Transformations and
Spatial Filtering 104
3.1 Background 105
3.1.1 The Basics of Intensity Transformations and Spatial Filtering 105
3.1.2 About the Examples in This Chapter 107
3.2 Some Basic Intensity Transformation Functions 107
3.2.1 Image Negatives 108
3.2.2 Log Transformations 109
3.2.3 Power-Law (Gamma) Transformations 110
3.2.4 Piecewise-Linear Transformation Functions 115
3.3 Histogram Processing 120
3.3.1 Histogram Equalization 122
3.3.2 Histogram Matching (Specification) 128
3.3.3 Local Histogram Processing 139
3.3.4 Using Histogram Statistics for Image Enhancement 139
3.4 Fundamentals of Spatial Filtering 144
3.4.1 The Mechanics of Spatial Filtering 145
3.4.2 Spatial Correlation and Convolution 146
3.4.3 Vector Representation of Linear Filtering 150
3.4.4 Generating Spatial Filter Masks 151
3.5 Smoothing Spatial Filters 152
3.5.1 Smoothing Linear Filters 152
3.5.2 Order-Statistic (Nonlinear) Filters 156
3.6 Sharpening Spatial Filters 157
3.6.1 Foundation 158
3.6.2 Using the Second Derivative for Image Sharpening—The
Laplacian 160</p>

<p>■ Contents vii
3.6.3 Unsharp Masking and Highboost Filtering 162
3.6.4 Using First-Order Derivatives for (Nonlinear) Image
Sharpening—The Gradient 165
3.7 Combining Spatial Enhancement Methods 169
3.8 Using Fuzzy Techniques for Intensity Transformations and Spatial
Filtering 173
3.8.1 Introduction 173
3.8.2 Principles of Fuzzy Set Theory 174
3.8.3 Using Fuzzy Sets 178
3.8.4 Using Fuzzy Sets for Intensity Transformations 186
3.8.5 Using Fuzzy Sets for Spatial Filtering 189
Summary 192
References and Further Reading 192
Problems 193
4
Filtering in the Frequency Domain 199
4.1 Background 200
4.1.1 ABrief History of the Fourier Series and Transform 200
4.1.2 About the Examples in this Chapter 201
4.2 Preliminary Concepts 202
4.2.1 Complex Numbers 202
4.2.2 Fourier Series 203
4.2.3 Impulses and Their Sifting Property 203
4.2.4 The Fourier Transform of Functions of One Continuous
Variable 205
4.2.5 Convolution 209
4.3 Sampling and the Fourier Transform of Sampled Functions 211
4.3.1 Sampling 211
4.3.2 The Fourier Transform of Sampled Functions 212
4.3.3 The Sampling Theorem 213
4.3.4 Aliasing 217
4.3.5 Function Reconstruction (Recovery) from Sampled Data 219
4.4 The Discrete Fourier Transform (DFT) of One Variable 220
4.4.1 Obtaining the DFT from the Continuous Transform of a
Sampled Function 221
4.4.2 Relationship Between the Sampling and Frequency
Intervals 223
4.5 Extension to Functions of Two Variables 225
4.5.1 The 2-D Impulse and Its Sifting Property 225
4.5.2 The 2-D Continuous Fourier Transform Pair 226
4.5.3 Two-Dimensional Sampling and the 2-D Sampling
Theorem 227
4.5.4 Aliasing in Images 228
4.5.5 The 2-D Discrete Fourier Transform and Its Inverse 235</p>

<p>viii ■ Contents
4.6 Some Properties of the 2-D Discrete Fourier Transform 236
4.6.1 Relationships Between Spatial and Frequency Intervals 236
4.6.2 Translation and Rotation 236
4.6.3 Periodicity 237
4.6.4 Symmetry Properties 239
4.6.5 Fourier Spectrum and Phase Angle 245
4.6.6 The 2-D Convolution Theorem 249
4.6.7 Summary of 2-D Discrete Fourier Transform Properties 253
4.7 The Basics of Filtering in the Frequency Domain 255
4.7.1 Additional Characteristics of the Frequency Domain 255
4.7.2 Frequency Domain Filtering Fundamentals 257
4.7.3 Summary of Steps for Filtering in the Frequency Domain 263
4.7.4 Correspondence Between Filtering in the Spatial and Frequency
Domains 263
4.8 Image Smoothing Using Frequency Domain Filters 269
4.8.1 Ideal Lowpass Filters 269
4.8.2 Butterworth Lowpass Filters 273
4.8.3 Gaussian Lowpass Filters 276
4.8.4 Additional Examples of Lowpass Filtering 277
4.9 Image Sharpening Using Frequency Domain Filters 280
4.9.1 Ideal Highpass Filters 281
4.9.2 Butterworth Highpass Filters 284
4.9.3 Gaussian Highpass Filters 285
4.9.4 The Laplacian in the Frequency Domain 286
4.9.5 Unsharp Masking, Highboost Filtering, and High-Frequency-
Emphasis Filtering 288
4.9.6 Homomorphic Filtering 289
4.10 Selective Filtering 294
4.10.1 Bandreject and Bandpass Filters 294
4.10.2 Notch Filters 294
4.11 Implementation 298
4.11.1 Separability of the 2-D DFT 298
4.11.2 Computing the IDFT Using a DFT Algorithm 299
4.11.3 The Fast Fourier Transform (FFT) 299
4.11.4 Some Comments on Filter Design 303
Summary 303
References and Further Reading 304
Problems 304
5
Image Restoration and Reconstruction 311
5.1 AModel of the Image Degradation/Restoration Process 312
5.2 Noise Models 313
5.2.1 Spatial and Frequency Properties of Noise 313
5.2.2 Some Important Noise Probability Density Functions 314</p>

<p>■ Contents ix
5.2.3 Periodic Noise 318
5.2.4 Estimation of Noise Parameters 319
5.3 Restoration in the Presence of Noise Only—Spatial Filtering 322
5.3.1 Mean Filters 322
5.3.2 Order-Statistic Filters 325
5.3.3 Adaptive Filters 330
5.4 Periodic Noise Reduction by Frequency Domain Filtering 335
5.4.1 Bandreject Filters 335
5.4.2 Bandpass Filters 336
5.4.3 Notch Filters 337
5.4.4 Optimum Notch Filtering 338
5.5 Linear, Position-Invariant Degradations 343
5.6 Estimating the Degradation Function 346
5.6.1 Estimation by Image Observation 346
5.6.2 Estimation by Experimentation 347
5.6.3 Estimation by Modeling 347
5.7 Inverse Filtering 351
5.8 Minimum Mean Square Error (Wiener) Filtering 352
5.9 Constrained Least Squares Filtering 357
5.10 Geometric Mean Filter 361
5.11 Image Reconstruction from Projections 362
5.11.1 Introduction 362
5.11.2 Principles of Computed Tomography (CT) 365
5.11.3 Projections and the Radon Transform 368
5.11.4 The Fourier-Slice Theorem 374
5.11.5 Reconstruction Using Parallel-Beam Filtered Backprojections
375
5.11.6 Reconstruction Using Fan-Beam Filtered Backprojections 381
Summary 387
References and Further Reading 388
Problems 389
6
Color Image Processing 394
6.1 Color Fundamentals 395
6.2 Color Models 401
6.2.1 The RGB Color Model 402
6.2.2 The CMYand CMYK Color Models 406
6.2.3 The HSI Color Model 407
6.3 Pseudocolor Image Processing 414
6.3.1 Intensity Slicing 415
6.3.2 Intensity to Color Transformations 418
6.4 Basics of Full-Color Image Processing 424
6.5 Color Transformations 426
6.5.1 Formulation 426
6.5.2 Color Complements 430</p>

<p>x ■ Contents
6.5.3 Color Slicing 431
6.5.4 Tone and Color Corrections 433
6.5.5 Histogram Processing 438
6.6 Smoothing and Sharpening 439
6.6.1 Color Image Smoothing 439
6.6.2 Color Image Sharpening 442
6.7 Image Segmentation Based on Color 443
6.7.1 Segmentation in HSI Color Space 443
6.7.2 Segmentation in RGB Vector Space 445
6.7.3 Color Edge Detection 447
6.8 Noise in Color Images 451
6.9 Color Image Compression 454
Summary 455
References and Further Reading 456
Problems 456
7
Wavelets and Multiresolution Processing 461
7.1 Background 462
7.1.1 Image Pyramids 463
7.1.2 Subband Coding 466
7.1.3 The Haar Transform 474
7.2 Multiresolution Expansions 477
7.2.1 Series Expansions 477
7.2.2 Scaling Functions 479
7.2.3 Wavelet Functions 483
7.3 Wavelet Transforms in One Dimension 486
7.3.1 The Wavelet Series Expansions 486
7.3.2 The Discrete Wavelet Transform 488
7.3.3 The Continuous Wavelet Transform 491
7.4 The Fast Wavelet Transform 493
7.5 Wavelet Transforms in Two Dimensions 501
7.6 Wavelet Packets 510
Summary 520
References and Further Reading 520
Problems 521
8
Image Compression 525
8.1 Fundamentals 526
8.1.1 Coding Redundancy 528
8.1.2 Spatial and Temporal Redundancy 529
8.1.3 Irrelevant Information 530
8.1.4 Measuring Image Information 531
8.1.5 Fidelity Criteria 534</p>

<p>■ Contents xi
8.1.6 Image Compression Models 536
8.1.7 Image Formats, Containers, and Compression Standards 538
8.2 Some Basic Compression Methods 542
8.2.1 Huffman Coding 542
8.2.2 Golomb Coding 544
8.2.3 Arithmetic Coding 548
8.2.4 LZW Coding 551
8.2.5 Run-Length Coding 553
8.2.6 Symbol-Based Coding 559
8.2.7 Bit-Plane Coding 562
8.2.8 Block Transform Coding 566
8.2.9 Predictive Coding 584
8.2.10 Wavelet Coding 604
8.3 Digital Image Watermarking 614
Summary 621
References and Further Reading 622
Problems 623
9
Morphological Image Processing 627
9.1 Preliminaries 628
9.2 Erosion and Dilation 630
9.2.1 Erosion 631
9.2.2 Dilation 633
9.2.3 Duality 635
9.3 Opening and Closing 635
9.4 The Hit-or-Miss Transformation 640
9.5 Some Basic Morphological Algorithms 642
9.5.1 Boundary Extraction 642
9.5.2 Hole Filling 643
9.5.3 Extraction of Connected Components 645
9.5.4 Convex Hull 647
9.5.5 Thinning 649
9.5.6 Thickening 650
9.5.7 Skeletons 651
9.5.8 Pruning 654
9.5.9 Morphological Reconstruction 656
9.5.10 Summary of Morphological Operations on Binary Images 664
9.6 Gray-Scale Morphology 665
9.6.1 Erosion and Dilation 666
9.6.2 Opening and Closing 668
9.6.3 Some Basic Gray-Scale Morphological Algorithms 670
9.6.4 Gray-Scale Morphological Reconstruction 676
Summary 679
References and Further Reading 679
Problems 680</p>

<p>xii ■ Contents
10
Image Segmentation 689
10.1 Fundamentals 690
10.2 Point, Line, and Edge Detection 692
10.2.1 Background 692
10.2.2 Detection of Isolated Points 696
10.2.3 Line Detection 697
10.2.4 Edge Models 700
10.2.5 Basic Edge Detection 706
10.2.6 More Advanced Techniques for Edge Detection 714
10.2.7 Edge Linking and Boundary Detection 725
10.3 Thresholding 738
10.3.1 Foundation 738
10.3.2 Basic Global Thresholding 741
10.3.3 Optimum Global Thresholding Using Otsu’s Method 742
10.3.4 Using Image Smoothing to Improve Global Thresholding 747
10.3.5 Using Edges to Improve Global Thresholding 749
10.3.6 Multiple Thresholds 752
10.3.7 Variable Thresholding 756
10.3.8 Multivariable Thresholding 761
10.4 Region-Based Segmentation 763
10.4.1 Region Growing 763
10.4.2 Region Splitting and Merging 766
10.5 Segmentation Using Morphological Watersheds 769
10.5.1 Background 769
10.5.2 Dam Construction 772
10.5.3 Watershed Segmentation Algorithm 774
10.5.4 The Use of Markers 776
10.6 The Use of Motion in Segmentation 778
10.6.1 Spatial Techniques 778
10.6.2 Frequency Domain Techniques 782
Summary 785
References and Further Reading 785
Problems 787
11
Representation and Description 795
11.1 Representation 796
11.1.1 Boundary (Border) Following 796
11.1.2 Chain Codes 798
11.1.3 Polygonal Approximations Using Minimum-Perimeter
Polygons 801
11.1.4 Other Polygonal Approximation Approaches 807
11.1.5 Signatures 808</p>

<p>■ Contents xiii
11.1.6 Boundary Segments 810
11.1.7 Skeletons 812
11.2 Boundary Descriptors 815
11.2.1 Some Simple Descriptors 815
11.2.2 Shape Numbers 816
11.2.3 Fourier Descriptors 818
11.2.4 Statistical Moments 821
11.3 Regional Descriptors 822
11.3.1 Some Simple Descriptors 822
11.3.2 Topological Descriptors 823
11.3.3 Texture 827
11.3.4 Moment Invariants 839
11.4 Use of Principal Components for Description 842
11.5 Relational Descriptors 852
Summary 856
References and Further Reading 856
Problems 857
12
Object Recognition 861
12.1 Patterns and Pattern Classes 861
12.2 Recognition Based on Decision-Theoretic Methods 866
12.2.1 Matching 866
12.2.2 Optimum Statistical Classifiers 872
12.2.3 Neural Networks 882
12.3 Structural Methods 903
12.3.1 Matching Shape Numbers 903
12.3.2 String Matching 904
Summary 906
References and Further Reading 906
Problems 907
Appendix A 910
Bibliography 915
Index 943</p>

<p>This page intentionally left blank</p>

<p>Preface
When something can be read without effort,
great effort has gone into its writing.
Enrique Jardiel Poncela
This edition of Digital Image Processingis a major revision of the book.As in
the 1977 and 1987 editions by Gonzalez and Wintz,and the 1992 and 2002 edi-
tions by Gonzalez and Woods,this fifth-generation edition was prepared with
students and instructors in mind.The principal objectives of the book continue
to be to provide an introduction to basic concepts and methodologies for digi-
tal image processing,and to develop a foundation that can be used as the basis
for further study and research in this field.To achieve these objectives, we
focused again on material that we believe is fundamental and whose scope of
application is not limited to the solution of specialized problems.The mathe-
matical complexity of the book remains at a level well within the grasp of
college seniors and first-year graduate students who have introductory prepa-
ration in mathematical analysis,vectors,matrices,probability,statistics,linear
systems,and computer programming.The book Web site provides tutorials to
support readers needing a review of this background material.
One of the principal reasons this book has been the world leader in its field
for more than 30 years is the level of attention we pay to the changing educa-
tional needs of our readers.The present edition is based on the most extensive
survey we have ever conducted.The survey involved faculty,students,and in-
dependent readers of the book in 134 institutions from 32 countries.The major
findings of the survey indicated a need for:
● A more comprehensive introduction early in the book to the mathemati-
cal tools used in image processing.
● An expanded explanation of histogram processing techniques.
● Stating complex algorithms in step-by-step summaries.
● An expanded explanation of spatial correlation and convolution.
● An introduction to fuzzy set theory and its application to image processing.
● A revision of the material dealing with the frequency domain, starting
with basic principles and showing how the discrete Fourier transform fol-
lows from data sampling.
● Coverage of computed tomography (CT).
● Clarification of basic concepts in the wavelets chapter.
● A revision of the data compression chapter to include more video com-
pression techniques,updated standards,and watermarking.
● Expansion of the chapter on morphology to include morphological recon-
struction and a revision of gray-scale morphology.
xv</p>

<p>xvi ■ Preface
● Expansion of the coverage on image segmentation to include more ad-
vanced edge detection techniques such as Canny’s algorithm,and a more
comprehensive treatment of image thresholding.
● An update of the chapter dealing with image representation and description.
● Streamlining the material dealing with structural object recognition.
The new and reorganized material that resulted in the present edition is our
attempt at providing a reasonable degree of balance between rigor,clarity of
presentation, and the findings of the market survey, while at the same time
keeping the length of the book at a manageable level.The major changes in
this edition of the book are as follows.
Chapter 1:A few figures were updated and part of the text was rewritten to
correspond to changes in later chapters.
Chapter 2:Approximately 50%of this chapter was revised to include new
images and clearer explanations. Major revisions include a new section on
image interpolation and a comprehensive new section summarizing the
principal mathematical tools used in the book. Instead of presenting “dry”
mathematical concepts one after the other,however,we took this opportu-
nity to bring into Chapter 2 a number of image processing applications that
were scattered throughout the book. For example, image averaging and
image subtraction were moved to this chapter to illustrate arithmetic opera-
tions.This follows a trend we began in the second edition of the book to move
as many applications as possible early in the discussion not only as illustra-
tions,but also as motivation for students.After finishing the newly organized
Chapter 2,a reader will have a basic understanding of how digital images are
manipulated and processed.This is a solid platform upon which the rest of the
book is built.
Chapter 3: Major revisions of this chapter include a detailed discussion of
spatial correlation and convolution, and their application to image filtering
using spatial masks.We also found a consistent theme in the market survey
asking for numerical examples to illustrate histogram equalization and specifi-
cation,so we added several such examples to illustrate the mechanics of these
processing tools. Coverage of fuzzy sets and their application to image pro-
cessing was also requested frequently in the survey.We included in this chap-
ter a new section on the foundation of fuzzy set theory,and its application to
intensity transformations and spatial filtering,two of the principal uses of this
theory in image processing.
Chapter 4: The topic we heard most about in comments and suggestions
during the past four years dealt with the changes we made in Chapter 4from
the first to the second edition.Our objective in making those changes was to
simplify the presentation of the Fourier transform and the frequency domain.
Evidently,we went too far,and numerous users of the book complained that
the new material was too superficial.We corrected that problem in the present
edition.The material now begins with the Fourier transform of one continuous
variable and proceeds to derive the discrete Fourier transform starting with
basic concepts of sampling and convolution.A byproduct of the flow of this</p>

<p>■ Preface xvii
material is an intuitive derivation of the sampling theorem and its implica-
tions.The 1-D material is then extended to 2-D,where we give a number of ex-
amples to illustrate the effects of sampling on digital images,including aliasing
and moiré patterns.The 2-D discrete Fourier transform is then illustrated and
a number of important properties are derived and summarized.These con-
cepts are then used as the basis for filtering in the frequency domain.Finally,
we discuss implementation issues such as transform decomposition and the
derivation of a fast Fourier transform algorithm.At the end of this chapter,the
reader will have progressed from sampling of 1-D functions through a clear
derivation of the foundation of the discrete Fourier transform and some of its
most important uses in digital image processing.
Chapter 5:The major revision in this chapter was the addition of a section
dealing with image reconstruction from projections,with a focus on computed
tomography (CT).Coverage of CT starts with an intuitive example of the un-
derlying principles of image reconstruction from projections and the various
imaging modalities used in practice.We then derive the Radon transform and
the Fourier slice theorem and use them as the basis for formulating the con-
cept of filtered backprojections. Both parallel- and fan-beam reconstruction
are discussed and illustrated using several examples.Inclusion of this material
was long overdue and represents an important addition to the book.
Chapter 6:Revisions to this chapter were limited to clarifications and a few
corrections in notation.No new concepts were added.
Chapter 7: We received numerous comments regarding the fact that the
transition from previous chapters into wavelets was proving difficult for be-
ginners.Several of the foundation sections were rewritten in an effort to make
the material clearer.
Chapter 8:This chapter was rewritten completely to bring it up to date.New
coding techniques, expanded coverage of video, a revision of the section on
standards,and an introduction to image watermarking are among the major
changes.The new organization will make it easier for beginning students to
follow the material.
Chapter 9:The major changes in this chapter are the inclusion of a new sec-
tion on morphological reconstruction and a complete revision of the section
on gray-scale morphology.The inclusion of morphological reconstruction for
both binary and gray-scale images made it possible to develop more complex
and useful morphological algorithms than before.
Chapter 10:This chapter also underwent a major revision.The organization
is as before,but the new material includes greater emphasis on basic principles
as well as discussion of more advanced segmentation techniques.Edge models
are discussed and illustrated in more detail,as are properties of the gradient.
The Marr-Hildreth and Canny edge detectors are included to illustrate more
advanced edge detection techniques.The section on thresholding was rewritten
also to include Otsu’s method,an optimum thresholding technique whose pop-
ularity has increased significantly over the past few years.We introduced this
approach in favor of optimum thresholding based on the Bayes classifica-
tion rule,not only because it is easier to understand and implement,but also</p>

<p>xviii ■ Preface
because it is used considerably more in practice. The Bayes approach was
moved to Chapter 12,where the Bayes decision rule is discussed in more detail.
We also added a discussion on how to use edge information to improve thresh-
olding and several new adaptive thresholding examples.Except for minor clar-
ifications,the sections on morphological watersheds and the use of motion for
segmentation are as in the previous edition.
Chapter 11: The principal changes in this chapter are the inclusion of a
boundary-following algorithm, a detailed derivation of an algorithm to fit a
minimum-perimeter polygon to a digital boundary,and a new section on co-
occurrence matrices for texture description.Numerous examples in Sections
11.2and 11.3are new,as are all the examples in Section 11.4.
Chapter 12: Changes in this chapter include a new section on matching by
correlation and a new example on using the Bayes classifier to recognize re-
gions of interest in multispectral images.The section on structural classifica-
tion now limits discussion only to string matching.
All the revisions just mentioned resulted in over 400 new images,over 200
new line drawings and tables, and more than 80 new homework problems.
Where appropriate,complex processing procedures were summarized in the
form of step-by-step algorithm formats.The references at the end of all chap-
ters were updated also.
The book Web site,established during the launch of the second edition,has
been a success,attracting more than 20,000 visitors each month.The site was
redesigned and upgraded to correspond to the launch of this edition.For more
details on features and content, see The Book Web Site, following the
Acknowledgments.
This edition of Digital Image Processing is a reflection of how the educa-
tional needs of our readers have changed since 2002.As is usual in a project
such as this,progress in the field continues after work on the manuscript stops.
One of the reasons why this book has been so well accepted since it first ap-
peared in 1977 is its continued emphasis on fundamental concepts—an ap-
proach that,among other things,attempts to provide a measure of stability in
a rapidly-evolving body of knowledge.We have tried to follow the same prin-
ciple in preparing this edition of the book.
R.C.G.
R.E.W.</p>

<p>Acknowledgments
Weare indebted to a number of individuals in academic circles as well as in in-
dustry and government who have contributed to this edition of the book.Their
contributions have been important in so many different ways that we find it
difficult to acknowledge them in any other way but alphabetically.In particu-
lar, we wish to extend our appreciation to our colleagues Mongi A.Abidi,
Steven L.Eddins,Yongmin Kim,Bryan Morse,Andrew Oldroyd,Ali M.Reza,
Edgardo Felipe Riveron,Jose Ruiz Shulcloper,and Cameron H.G.Wright for
their many suggestions on how to improve the presentation and/or the scope
of coverage in the book.
Numerous individuals and organizations provided us with valuable assis-
tance during the writing of this edition.Again,we list them alphabetically.We
are particularly indebted to Courtney Esposito and Naomi Fernandes at The
Mathworks for providing us with MATLAB software and support that were
important in our ability to create or clarify many of the examples and experi-
mental results included in this edition of the book.A significant percentage of
the new images used in this edition (and in some cases their history and inter-
pretation) were obtained through the efforts of individuals whose contribu-
tions are sincerely appreciated. In particular, we wish to acknowledge the
efforts of Serge Beucher, Melissa D. Binde, James Blankenship, Uwe Boos,
Ernesto Bribiesca,Michael E.Casey,Michael W.Davidson,Susan L.Forsburg,
Thomas R.Gest,Lalit Gupta,Daniel A.Hammer,Zhong He,Roger Heady,
Juan A.Herrera,John M.Hudak,Michael Hurwitz,Chris J.Johannsen,Rhon-
da Knighton, Don P. Mitchell,Ashley Mohamed,A. Morris, Curtis C. Ober,
Joseph E.Pascente,David.R.Pickens,Michael Robinson,Barrett A.Schaefer,
Michael Shaffer, Pete Sites, Sally Stowe, Craig Watson, David K.Wehe, and
Robert A.West.We also wish to acknowledge other individuals and organiza-
tions cited in the captions of numerous figures throughout the book for their
permission to use that material.
Special thanks go to Vince O’Brien,Rose Kernan,Scott Disanno,Michael
McDonald,Joe Ruddick,Heather Scott,and Alice Dworkin,at Prentice Hall.
Their creativity, assistance, and patience during the production of this book
are truly appreciated.
R.C.G.
R.E.W.
xix</p>

<p>The Book Web Site
www.prenhall.com/gonzalezwoods
or its mirror site,
www.imageprocessingplace.com
Digital Image Processing is a completely self-contained book. However, the
companion Web site offers additional support in a number of important areas.
For the Student or Independent Readerthe site contains
● Reviews in areas such as probability,statistics,vectors,and matrices.
● Complete solutions to selected problems.
● Computer projects.
● A Tutorials section containing dozens of tutorials on most of the topics
discussed in the book.
● A database containing all the images in the book.
For the Instructorthe site contains
● AnInstructor’s Manualwith complete solutions to all the problems in the
book,as well as course and laboratory teaching guidelines.The manual is
available free of charge to instructors who have adopted the book for
classroom use.
● Classroom presentation materials in PowerPoint format.
● Material removed from previous editions, downloadable in convenient
PDF format.
● Numerous links to other educational resources.
For the Practitionerthe site contains additional specialized topics such as
● Links to commercial sites.
● Selected new references.
● Links to commercial image databases.
The Web site is an ideal tool for keeping the book current between editions by
including new topics,digital images,and other relevant material that has ap-
peared after the book was published.Although considerable care was taken in
the production of the book,the Web site is also a convenient repository for any
errors that may be discovered between printings.References to the book Web
site are designated in the book by the following icon:
xx</p>

<p>About the Authors
Rafael C. Gonzalez
R.C.Gonzalez received the B.S.E.E.degree from the University of Miami in
1965 and the M.E.and Ph.D.degrees in electrical engineering from the Univer-
sity of Florida,Gainesville,in 1967 and 1970,respectively.He joined the Elec-
trical and Computer Engineering Department at the University of Tennessee,
Knoxville (UTK) in 1970,where he became Associate Professor in 1973,Pro-
fessor in 1978,and Distinguished Service Professor in 1984.He served as Chair-
man of the department from 1994 through 1997. He is currently a Professor
Emeritus at UTK.
Gonzalez is the founder of the Image &amp; Pattern Analysis Laboratory and the
Robotics &amp; Computer Vision Laboratory at the University of Tennessee. He
also founded Perceptics Corporation in 1982 and was its president until 1992.
The last three years of this period were spent under a full-time employment con-
tract with Westinghouse Corporation,who acquired the company in 1989.
Under his direction,Perceptics became highly successful in image process-
ing,computer vision,and laser disk storage technology.In its initial ten years,
Perceptics introduced a series of innovative products,including:The world’s
first commercially-available computer vision system for automatically reading
license plates on moving vehicles;a series of large-scale image processing and
archiving systems used by the U.S.Navy at six different manufacturing sites
throughout the country to inspect the rocket motors of missiles in the Trident
II Submarine Program;the market-leading family of imaging boards for ad-
vanced Macintosh computers;and a line of trillion-byte laser disk products.
He is a frequent consultant to industry and government in the areas of pat-
tern recognition,image processing,and machine learning.His academic hon-
ors for work in these fields include the 1977 UTK College of Engineering
Faculty Achievement Award; the 1978 UTK Chancellor’s Research Scholar
Award;the 1980 Magnavox Engineering Professor Award;and the 1980 M.E.
Brooks Distinguished Professor Award.In 1981 he became an IBM Professor
at the University of Tennessee and in 1984 he was named a Distinguished Ser-
vice Professor there.He was awarded a Distinguished Alumnus Award by the
University of Miami in 1985,the Phi Kappa Phi Scholar Award in 1986,and
the University of Tennessee’s Nathan W.Dougherty Award for Excellence in
Engineering in 1992.
Honors for industrial accomplishment include the 1987 IEEE Outstanding
Engineer Award for Commercial Development in Tennessee;the 1988 Albert
Rose Nat’l Award for Excellence in Commercial Image Processing;the 1989 B.
Otto Wheeley Award for Excellence in Technology Transfer;the 1989 Coopers
and Lybrand Entrepreneur of the Year Award;the 1992 IEEE Region 3 Out-
standing Engineer Award;and the 1993 Automated Imaging Association Na-
tional Award for Technology Development.
xxi</p>

<p>xxii ■ About the Authors
Gonzalez is author or co-author of over 100 technical articles,two edited
books,and four textbooks in the fields of pattern recognition,image process-
ing,and robotics.His books are used in over 1000 universities and research in-
stitutions throughout the world.He is listed in the prestigious Marquis Who’s
Who in America,MarquisWho’s Who in Engineering,MarquisWho’s Who in
the World,and in 10 other national and international biographical citations.He
is the co-holder of two U.S.Patents,and has been an associate editor of the
IEEE Transactions on Systems, Man and Cybernetics, and the International
Journal of Computer and Information Sciences.He is a member of numerous
professional and honorary societies,including Tau Beta Pi,Phi Kappa Phi,Eta
Kappa Nu,and Sigma Xi.He is a Fellow of the IEEE.
Richard E. Woods
Richard E. Woods earned his B.S., M.S., and Ph.D. degrees in Electrical
Engineering from the University of Tennessee,Knoxville.His professional
experiences range from entrepreneurial to the more traditional academic,
consulting, governmental, and industrial pursuits. Most recently, he founded
MedData Interactive,a high technology company specializing in the develop-
ment of handheld computer systems for medical applications.He was also a
founder and Vice President of Perceptics Corporation,where he was responsi-
ble for the development of many of the company’s quantitative image analysis
and autonomous decision-making products.
Prior to Perceptics and MedData,Dr.Woods was an Assistant Professor of
Electrical Engineering and Computer Science at the University of Tennessee
and prior to that,a computer applications engineer at Union Carbide Corpo-
ration.As a consultant,he has been involved in the development of a number
of special-purpose digital processors for a variety of space and military agen-
cies, including NASA, the Ballistic Missile Systems Command, and the Oak
Ridge National Laboratory.
Dr.Woods has published numerous articles related to digital signal process-
ing and is a member of several professional societies,including Tau Beta Pi,
Phi Kappa Phi,and the IEEE.In 1986,he was recognized as a Distinguished
Engineering Alumnus of the University of Tennessee.</p>

<p>1
Introduction
One picture is worth more than ten thousand words.
Anonymous
Preview
Interest in digital image processing methods stems from two principal applica-
tion areas:improvement of pictorial information for human interpretation;and
processing of image data for storage,transmission,and representation for au-
tonomous machine perception.This chapter has several objectives:(1) to define
the scope of the field that we call image processing;(2) to give a historical per-
spective of the origins of this field;(3) to give you an idea of the state of the art
in image processing by examining some of the principal areas in which it is ap-
plied;(4) to discuss briefly the principal approaches used in digital image pro-
cessing; (5) to give an overview of the components contained in a typical,
general-purpose image processing system;and (6) to provide direction to the
books and other literature where image processing work normally is reported.
1.1 What Is Digital Image Processing?
An image may be defined as a two-dimensional function,f(x,y),where xand
yarespatial(plane) coordinates,and the amplitude of fat any pair of coordi-
nates (x,y)is called the intensityorgray levelof the image at that point.When
x,y,and the intensity values of f are all finite,discrete quantities,we call the
image a digital image.The field of digital image processingrefers to processing
digital images by means of a digital computer.Note that a digital image is com-
posed of a finite number of elements,each of which has a particular location
1</p>

<p>2 Chapter 1 ■ Introduction
and value.These elements are called picture elements,image elements,pels,and
pixels.Pixel is the term used most widely to denote the elements of a digital
image.We consider these definitions in more formal terms in Chapter 2.
Vision is the most advanced of our senses,so it is not surprising that images
play the single most important role in human perception.However,unlike hu-
mans,who are limited to the visual band of the electromagnetic (EM) spec-
trum,imaging machines cover almost the entire EM spectrum,ranging from
gamma to radio waves.They can operate on images generated by sources that
humans are not accustomed to associating with images.These include ultra-
sound, electron microscopy, and computer-generated images. Thus, digital
image processing encompasses a wide and varied field of applications.
There is no general agreement among authors regarding where image
processing stops and other related areas,such as image analysis and comput-
er vision,start.Sometimes a distinction is made by defining image processing
as a discipline in which both the input and output of a process are images.We
believe this to be a limiting and somewhat artificial boundary.For example,
under this definition,even the trivial task of computing the average intensity
of an image (which yields a single number) would not be considered an
image processing operation.On the other hand,there are fields such as com-
puter vision whose ultimate goal is to use computers to emulate human vi-
sion,including learning and being able to make inferences and take actions
based on visual inputs.This area itself is a branch of artificial intelligence
(AI) whose objective is to emulate human intelligence.The field of AI is in
its earliest stages of infancy in terms of development,with progress having
been much slower than originally anticipated. The area of image analysis
(also called image understanding) is in between image processing and com-
puter vision.
There are no clear-cut boundaries in the continuum from image processing
at one end to computer vision at the other.However,one useful paradigm is
to consider three types of computerized processes in this continuum: low-,
mid-,and high-level processes.Low-level processes involve primitive opera-
tions such as image preprocessing to reduce noise,contrast enhancement,and
image sharpening.A low-level process is characterized by the fact that both
its inputs and outputs are images. Mid-level processing on images involves
tasks such as segmentation (partitioning an image into regions or objects),de-
scription of those objects to reduce them to a form suitable for computer pro-
cessing, and classification (recognition) of individual objects. A mid-level
process is characterized by the fact that its inputs generally are images,but its
outputs are attributes extracted from those images (e.g.,edges,contours,and
the identity of individual objects). Finally, higher-level processing involves
“making sense”of an ensemble of recognized objects,as in image analysis,and,
at the far end of the continuum,performing the cognitive functions normally
associated with vision.
Based on the preceding comments,we see that a logical place of overlap be-
tween image processing and image analysis is the area of recognition of indi-
vidual regions or objects in an image.Thus,what we call in this book digital
image processingencompasses processes whose inputs and outputs are images</p>

<p>1.2 ■ The Origins of Digital Image Processing 3
and,in addition,encompasses processes that extract attributes from images,up
to and including the recognition of individual objects.As an illustration to clar-
ify these concepts, consider the area of automated analysis of text. The
processes of acquiring an image of the area containing the text,preprocessing
that image, extracting (segmenting) the individual characters, describing the
characters in a form suitable for computer processing,and recognizing those
individual characters are in the scope of what we call digital image processing
in this book.Making sense of the content of the page may be viewed as being in
the domain of image analysis and even computer vision,depending on the level
of complexity implied by the statement “making sense.”As will become evident
shortly,digital image processing,as we have defined it,is used successfully in a
broad range of areas of exceptional social and economic value.The concepts
developed in the following chapters are the foundation forthe methods used in
those application areas.
1.2 The Origins of Digital Image Processing
One of the first applications of digital images was in the newspaper indus-
try,when pictures were first sent by submarine cable between London and
New York. Introduction of the Bartlane cable picture transmission system
in the early 1920s reduced the time required to transport a picture across
the Atlantic from more than a week to less than three hours. Specialized
printing equipment coded pictures for cable transmission and then recon-
structed them at the receiving end. Figure 1.1 was transmitted in this way
and reproduced on a telegraph printer fitted with typefaces simulating a
halftone pattern.
Some of the initial problems in improving the visual quality of these early
digital pictures were related to the selection of printing procedures and the
distribution of intensity levels.The printing method used to obtain Fig.1.1was
abandoned toward the end of 1921 in favor of a technique based on photo-
graphic reproduction made from tapes perforated at the telegraph receiving
terminal.Figure 1.2shows an image obtained using this method.The improve-
ments over Fig.1.1are evident,both in tonal quality and in resolution.
FIGURE1.1 A
digital picture
produced in 1921
from a coded tape
by a telegraph
printer with
special type faces.
(McFarlane.†)
†References in the Bibliography at the end of the book are listed in alphabetical order by authors’ last
names.</p>

<p>4 Chapter 1 ■ Introduction
FIGURE1.2 A
digital picture
made in 1922
from a tape
punched after the
signals had
crossed the
Atlantic twice.
(McFarlane.)
The early Bartlane systems were capable of coding images in five distinct
levels of gray.This capability was increased to 15 levels in 1929.Figure 1.3 is
typical of the type of images that could be obtained using the 15-tone equip-
ment.During this period,introduction of a system for developing a film plate
via light beams that were modulated by the coded picture tape improved the
reproduction process considerably.
Although the examples just cited involve digital images,they are not con-
sidered digital image processing results in the context of our definition be-
cause computers were not involved in their creation. Thus, the history of
digital image processing is intimately tied to the development of the digital
computer.In fact,digital images require so much storage and computational
power that progress in the field of digital image processing has been depen-
dent on the development of digital computers and of supporting technologies
that include data storage,display,and transmission.
The idea of a computer goes back to the invention of the abacus in Asia
Minor,more than 5000 years ago.More recently,there were developments in
the past two centuries that are the foundation of what we call a computer today.
However,the basis for what we call a modern digital computer dates back to
only the 1940s with the introduction by John von Neumann of two key con-
cepts: (1) a memory to hold a stored program and data, and (2) conditional
branching. These two ideas are the foundation of a central processing unit
(CPU),which is at the heart of computers today.Starting with von Neumann,
there were a series of key advances that led to computers powerful enough to
FIGURE1.3
Unretouched
cable picture of
Generals Pershing
and Foch,
transmitted in
1929 from
London to New
York by 15-tone
equipment.
(McFarlane.)</p>

<p>1.2 ■ The Origins of Digital Image Processing 5
be used for digital image processing.Briefly,these advances may be summa-
rized as follows:(1) the invention of the transistor at Bell Laboratories in 1948;
(2) the development in the 1950s and 1960s of the high-level programming lan-
guages COBOL (Common Business-Oriented Language) and FORTRAN
(Formula Translator);(3) the invention of the integrated circuit (IC) at Texas
Instruments in 1958; (4) the development of operating systems in the early
1960s;(5) the development of the microprocessor (a single chip consisting of
the central processing unit,memory,and input and output controls) by Intel in
the early 1970s;(6) introduction by IBM of the personal computer in 1981;and
(7) progressive miniaturization of components,starting with large scale integra-
tion (LI) in the late 1970s,then very large scale integration (VLSI) in the 1980s,
to the present use of ultra large scale integration (ULSI). Concurrent with
these advances were developments in the areas of mass storage and display sys-
tems,both of which are fundamental requirements for digital image processing.
The first computers powerful enough to carry out meaningful image pro-
cessing tasks appeared in the early 1960s.The birth of what we call digital
image processing today can be traced to the availability of those machines and
to the onset of the space program during that period.It took the combination
of those two developments to bring into focus the potential of digital image
processing concepts.Work on using computer techniques for improving im-
ages from a space probe began at the Jet Propulsion Laboratory (Pasadena,
California) in 1964 when pictures of the moon transmitted by Ranger 7 were
processed by a computer to correct various types of image distortion inherent
in the on-board television camera. Figure 1.4 shows the first image of the
moon taken by Ranger 7on July 31,1964 at 9:09 A.M.Eastern Daylight Time
(EDT), about 17 minutes before impacting the lunar surface (the markers,
called reseau marks, are used for geometric corrections, as discussed in
Chapter 2).This also is the first image of the moon taken by a U.S.spacecraft.
The imaging lessons learned with Ranger 7 served as the basis for improved
methods used to enhance and restore images from the Surveyor missions to
the moon,the Mariner series of flyby missions to Mars,the Apollo manned
flights to the moon,and others.
FIGURE1.4 The
first picture of the
moon by a U.S.
spacecraft.Ranger
7took this image
on July 31,1964 at
9:09A.M.EDT,
about 17 minutes
before impacting
the lunar surface.
(Courtesy of
NASA.)</p>

<p>6 Chapter 1 ■ Introduction
In parallel with space applications, digital image processing techniques
began in the late 1960s and early 1970s to be used in medical imaging,remote
Earth resources observations,and astronomy.The invention in the early 1970s
of computerized axial tomography (CAT),also called computerized tomogra-
phy (CT) for short,is one of the most important events in the application of
image processing in medical diagnosis. Computerized axial tomography is a
process in which a ring of detectors encircles an object (or patient) and an
X-ray source,concentric with the detector ring,rotates about the object.The
X-rays pass through the object and are collected at the opposite end by the
corresponding detectors in the ring.As the source rotates,this procedure is re-
peated.Tomography consists of algorithms that use the sensed data to con-
struct an image that represents a “slice” through the object. Motion of the
object in a direction perpendicular to the ring of detectors produces a set of
such slices,which constitute a three-dimensional (3-D) rendition of the inside
of the object. Tomography was invented independently by Sir Godfrey
N.Hounsfield and Professor Allan M.Cormack,who shared the 1979 Nobel
Prize in Medicine for their invention.It is interesting to note that X-rays were
discovered in 1895 by Wilhelm Conrad Roentgen,for which he received the
1901 Nobel Prize for Physics.These two inventions,nearly 100 years apart,led
to some of the most important applications of image processing today.
From the 1960s until the present,the field of image processing has grown
vigorously.In addition to applications in medicine and the space program,dig-
ital image processing techniques now are used in a broad range of applica-
tions. Computer procedures are used to enhance the contrast or code the
intensity levels into color for easier interpretation of X-rays and other images
used in industry, medicine, and the biological sciences. Geographers use the
same or similar techniques to study pollution patterns from aerial and satellite
imagery.Image enhancement and restoration procedures are used to process
degraded images of unrecoverable objects or experimental results too expen-
sive to duplicate.In archeology,image processing methods have successfully
restored blurred pictures that were the only available records of rare artifacts
lost or damaged after being photographed.In physics and related fields,com-
puter techniques routinely enhance images of experiments in areas such as
high-energy plasmas and electron microscopy. Similarly successful applica-
tions of image processing concepts can be found in astronomy,biology,nuclear
medicine,law enforcement,defense,and industry.
These examples illustrate processing results intended for human interpreta-
tion.The second major area of application of digital image processing tech-
niques mentioned at the beginning of this chapter is in solving problems dealing
with machine perception.In this case,interest is on procedures for extracting
from an image information in a form suitable for computer processing.Often,
this information bears little resemblance to visual features that humans use in
interpreting the content of an image.Examples of the type of information used
in machine perception are statistical moments,Fourier transform coefficients,
and multidimensional distance measures.Typical problems in machine percep-
tion that routinely utilize image processing techniques are automatic character
recognition, industrial machine vision for product assembly and inspection,</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 7
military recognizance,automatic processing of fingerprints,screening of X-rays
and blood samples,and machine processing of aerial and satellite imagery for
weather prediction and environmental assessment.The continuing decline in the
ratio of computer price to performance and the expansion of networking and
communication bandwidth via the World Wide Web and the Internet have cre-
ated unprecedented opportunities for continued growth of digital image pro-
cessing.Some of these application areas are illustrated in the following section.
1.3 Examples of Fields that Use Digital Image Processing
Today,there is almost no area of technical endeavor that is not impacted in
some way by digital image processing.We can cover only a few of these appli-
cations in the context and space of the current discussion.However,limited as
it is,the material presented in this section will leave no doubt in your mind re-
garding the breadth and importance of digital image processing.We show in
this section numerous areas of application,each of which routinely utilizes the
digital image processing techniques developed in the following chapters.Many
of the images shown in this section are used later in one or more of the exam-
ples given in the book.All images shown are digital.
The areas of application of digital image processing are so varied that some
form of organization is desirable in attempting to capture the breadth of this
field.One of the simplest ways to develop a basic understanding of the extent of
image processing applications is to categorize images according to their source
(e.g.,visual,X-ray,and so on).The principal energy source for images in use today
is the electromagnetic energy spectrum.Other important sources of energy in-
clude acoustic,ultrasonic,and electronic (in the form of electron beams used in
electron microscopy).Synthetic images,used for modeling and visualization,are
generated by computer.In this section we discuss briefly how images are gener-
ated in these various categories and the areas in which they are applied.Methods
for converting images into digital form are discussed in the next chapter.
Images based on radiation from the EM spectrum are the most familiar,
especially images in the X-ray and visual bands of the spectrum.Electromag-
netic waves can be conceptualized as propagating sinusoidal waves of varying
wavelengths,or they can be thought of as a stream of massless particles,each
traveling in a wavelike pattern and moving at the speed of light.Each mass-
less particle contains a certain amount (or bundle) of energy.Each bundle of
energy is called a photon.If spectral bands are grouped according to energy
per photon,we obtain the spectrum shown in Fig.1.5,ranging from gamma
rays (highest energy) at one end to radio waves (lowest energy) at the other.
Energy of one photon (electron volts)
106 105 104 103 102 101 100 10(cid:1)1 10(cid:1)2 10(cid:1)3 10(cid:1)4 10(cid:1)5 10(cid:1)6 10(cid:1)7 10(cid:1)8 10(cid:1)9
Gamma rays X-rays Ultraviolet Visible Infrared Microwaves Radio waves
FIGURE1.5 The electromagnetic spectrum arranged according to energy per photon.</p>

<p>8 Chapter 1 ■ Introduction
The bands are shown shaded to convey the fact that bands of the EM spec-
trum are not distinct but rather transition smoothly from one to the other.
1.3.1 Gamma-Ray Imaging
Major uses of imaging based on gamma rays include nuclear medicine and as-
tronomical observations.In nuclear medicine,the approach is to inject a pa-
tient with a radioactive isotope that emits gamma rays as it decays.Images are
produced from the emissions collected by gamma ray detectors.Figure 1.6(a)
shows an image of a complete bone scan obtained by using gamma-ray imaging.
Images of this sort are used to locate sites of bone pathology,such as infections
a b
c d
FIGURE1.6
Examples of
gamma-ray
imaging.(a) Bone
scan.(b) PET
image.(c) Cygnus
Loop.(d) Gamma
radiation (bright
spot) from a
reactor valve.
(Images courtesy
of (a) G.E.
Medical Systems,
(b) Dr.Michael
E.Casey,CTI
PET Systems,
(c) NASA,
(d) Professors
Zhong He and
David K.Wehe,
University of
Michigan.)</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 9
or tumors. Figure 1.6(b) shows another major modality of nuclear imaging
called positron emission tomography (PET).The principle is the same as with
X-ray tomography,mentioned briefly in Section 1.2.However,instead of using
an external source of X-ray energy,the patient is given a radioactive isotope
that emits positrons as it decays.When a positron meets an electron,both are
annihilated and two gamma rays are given off.These are detected and a tomo-
graphic image is created using the basic principles of tomography.The image
shown in Fig.1.6(b)is one sample of a sequence that constitutes a 3-D rendition
of the patient.This image shows a tumor in the brain and one in the lung,easily
visible as small white masses.
A star in the constellation of Cygnus exploded about 15,000 years ago,gener-
ating a superheated stationary gas cloud (known as the Cygnus Loop) that glows
in a spectacular array of colors.Figure 1.6(c)shows an image of the Cygnus Loop
in the gamma-ray band. Unlike the two examples in Figs. 1.6(a) and (b), this
image was obtained using the natural radiation of the object being imaged.Finally,
Fig.1.6(d)shows an image of gamma radiation from a valve in a nuclear reactor.
An area of strong radiation is seen in the lower left side of the image.
1.3.2 X-Ray Imaging
X-rays are among the oldest sources of EM radiation used for imaging.The
best known use of X-rays is medical diagnostics,but they also are used exten-
sively in industry and other areas,like astronomy.X-rays for medical and in-
dustrial imaging are generated using an X-ray tube,which is a vacuum tube
with a cathode and anode.The cathode is heated,causing free electrons to be
released.These electrons flow at high speed to the positively charged anode.
When the electrons strike a nucleus,energy is released in the form of X-ray
radiation.The energy (penetrating power) of X-rays is controlled by a voltage
applied across the anode, and by a current applied to the filament in the
cathode.Figure 1.7(a)shows a familiar chest X-ray generated simply by plac-
ing the patient between an X-ray source and a film sensitive to X-ray energy.
The intensity of the X-rays is modified by absorption as they pass through the
patient,and the resulting energy falling on the film develops it,much in the
same way that light develops photographic film.In digital radiography,digital
images are obtained by one of two methods:(1) by digitizing X-ray films;or
(2) by having the X-rays that pass through the patient fall directly onto devices
(such as a phosphor screen) that convert X-rays to light.The light signal in
turn is captured by a light-sensitive digitizing system.We discuss digitization
in more detail in Chapters 2and 4.
Angiography is another major application in an area called contrast-
enhancement radiography. This procedure is used to obtain images (called
angiograms) of blood vessels.A catheter (a small,flexible,hollow tube) is in-
serted,for example,into an artery or vein in the groin.The catheter is threaded
into the blood vessel and guided to the area to be studied.When the catheter
reaches the site under investigation, an X-ray contrast medium is injected
through the tube.This enhances contrast of the blood vessels and enables the
radiologist to see any irregularities or blockages.Figure 1.7(b)shows an exam-
ple of an aortic angiogram.The catheter can be seen being inserted into the</p>

<p>10 Chapter 1 ■ Introduction
a FIGURE1.7 Examples of X-ray imaging.(a) Chest X-ray.(b) Aortic angiogram.(c) Head
d
b CT. (d) Circuit boards. (e) Cygnus Loop. (Images courtesy of (a) and (c) Dr. David
c e R.Pickens,Dept.of Radiology &amp; Radiological Sciences,Vanderbilt University Medical
Center;(b) Dr.Thomas R.Gest,Division of Anatomical Sciences,University of Michigan
Medical School;(d) Mr.Joseph E.Pascente,Lixi,Inc.;and (e) NASA.)</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 11
large blood vessel on the lower left of the picture.Note the high contrast of the
large vessel as the contrast medium flows up in the direction of the kidneys,
which are also visible in the image.As discussed in Chapter 2,angiography is a
major area of digital image processing,where image subtraction is used to en-
hance further the blood vessels being studied.
Another important use of X-rays in medical imaging is computerized axial to-
mography (CAT).Due to their resolution and 3-D capabilities,CAT scans revo-
lutionized medicine from the moment they first became available in the early
1970s.As noted in Section 1.2,each CAT image is a “slice”taken perpendicularly
through the patient.Numerous slices are generated as the patient is moved in a
longitudinal direction.The ensemble of such images constitutes a 3-D rendition of
the inside of the body,with the longitudinal resolution being proportional to the
number of slice images taken.Figure 1.7(c)shows a typical head CAT slice image.
Techniques similar to the ones just discussed,but generally involving higher-
energy X-rays,are applicable in industrial processes.Figure 1.7(d)shows an X-ray
image of an electronic circuit board.Such images,representative of literally hun-
dreds of industrial applications of X-rays,are used to examine circuit boards for
flaws in manufacturing,such as missing components or broken traces.Industrial
CAT scans are useful when the parts can be penetrated by X-rays,such as in
plastic assemblies, and even large bodies, like solid-propellant rocket motors.
Figure 1.7(e)shows an example of X-ray imaging in astronomy.This image is the
Cygnus Loop of Fig.1.6(c),but imaged this time in the X-ray band.
1.3.3 Imaging in the Ultraviolet Band
Applications of ultraviolet “light”are varied.They include lithography,industrial
inspection,microscopy,lasers,biological imaging,and astronomical observations.
Weillustrate imaging in this band with examples from microscopy and astronomy.
Ultraviolet light is used in fluorescence microscopy,one of the fastest grow-
ing areas of microscopy.Fluorescence is a phenomenon discovered in the mid-
dle of the nineteenth century, when it was first observed that the mineral
fluorspar fluoresces when ultraviolet light is directed upon it.The ultraviolet
light itself is not visible,but when a photon ofultraviolet radiation collides with
an electron in an atom of a fluorescent material,it elevates the electron to a higher
energy level.Subsequently,the excited electron relaxes to a lower level and emits
light in the form of a lower-energy photon in the visible (red) light region.The
basic task of the fluorescence microscope is to use an excitation light to irradiate
a prepared specimen and then to separate the much weaker radiating fluores-
cent light from the brighter excitation light.Thus,only the emission light reaches
the eye or other detector.The resulting fluorescing areas shine against a dark
background with sufficient contrast to permit detection.The darker the back-
ground of the nonfluorescing material,the more efficient the instrument.
Fluorescence microscopy is an excellent method for studying materials that
can be made to fluoresce,either in their natural form (primary fluorescence) or
when treated with chemicals capable of fluorescing (secondary fluorescence).
Figures 1.8(a) and (b) show results typical of the capability of fluorescence
microscopy.Figure 1.8(a) shows a fluorescence microscope image of normal
corn,and Fig.1.8(b) shows corn infected by “smut,”a disease of cereals,corn,</p>

<p>12 Chapter 1 ■ Introduction
a b
c
FIGURE1.8
Examples of
ultraviolet
imaging.
(a) Normal corn.
(b) Smut corn.
(c) Cygnus Loop.
(Images courtesy
of (a) and
(b) Dr.Michael
W.Davidson,
Florida State
University,
(c) NASA.)
grasses,onions,and sorghum that can be caused by any of more than 700 species
of parasitic fungi.Corn smut is particularly harmful because corn is one of the
principal food sources in the world.As another illustration,Fig.1.8(c)shows the
Cygnus Loop imaged in the high-energy region of the ultraviolet band.
1.3.4 Imaging in the Visible and Infrared Bands
Considering that the visual band of the electromagnetic spectrum is the most
familiar in all our activities,it is not surprising that imaging in this band out-
weighs by far all the others in terms of breadth of application.The infrared
band often is used in conjunction with visual imaging,so we have grouped the</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 13
visible and infrared bands in this section for the purpose of illustration.We
consider in the following discussion applications in light microscopy,astrono-
my,remote sensing,industry,and law enforcement.
Figure 1.9shows several examples of images obtained with a light microscope.
The examples range from pharmaceuticals and microinspection to materials
characterization.Even in microscopy alone,the application areas are too numer-
ous to detail here.It is not difficult to conceptualize the types of processes one
might apply to these images,ranging from enhancement to measurements.
a b c
d e f
FIGURE1.9 Examples of light microscopy images. (a) Taxol (anticancer agent),
magnified 250<em>. (b) Cholesterol—40</em>. (c) Microprocessor—60<em>. (d) Nickel oxide
thin film—600</em>. (e) Surface of audio CD—1750<em>. (f) Organic superconductor—
450</em>.(Images courtesy of Dr.Michael W.Davidson,Florida State University.)</p>

<p>14 Chapter 1 ■ Introduction
TABLE 1.1 Band No. Name Wavelength ((cid:1)m) Characteristics and Uses
Thematic bands
in NASA’s 1 Visible blue 0.45–0.52 Maximum water
LANDSAT penetration
satellite. 2 Visible green 0.52–0.60 Good for measuring plant
vigor
3 Visible red 0.63–0.69 Vegetation discrimination
4 Near infrared 0.76–0.90 Biomass and shoreline
mapping
5 Middle infrared 1.55–1.75 Moisture content of soil
and vegetation
6 Thermal infrared 10.4–12.5 Soil moisture;thermal
mapping
7 Middle infrared 2.08–2.35 Mineral mapping
Another major area of visual processing is remote sensing,which usually in-
cludes several bands in the visual and infrared regions of the spectrum.Table 1.1
shows the so-called thematic bandsin NASA’s LANDSAT satellite.The primary
function of LANDSAT is to obtain and transmit images of the Earth from space
for purposes of monitoring environmental conditions on the planet.The bands
are expressed in terms of wavelength,with 1(cid:2)m being equal to 10-6 m(we dis-
cuss the wavelength regions of the electromagnetic spectrum in more detail in
Chapter 2).Note the characteristics and uses of each band in Table 1.1.
In order to develop a basic appreciation for the power of this type of
multispectral imaging,consider Fig.1.10,which shows one image for each of
1 2 3
4 5 6 7
FIGURE1.10 LANDSAT satellite images of the Washington,D.C.area.The numbers refer to the thematic
bands in Table 1.1.(Images courtesy of NASA.)</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 15
FIGURE1.11
Satellite image
of Hurricane
Katrina taken on
August 29,2005.
(Courtesy of
NOAA.)
the spectral bands in Table 1.1.The area imaged is Washington D.C.,which in-
cludes features such as buildings,roads,vegetation,and a major river (the Po-
tomac) going though the city.Images of population centers are used routinely
(over time) to assess population growth and shift patterns,pollution,and other
factors harmful to the environment.The differences between visual and in-
frared image features are quite noticeable in these images.Observe,for exam-
ple,how well defined the river is from its surroundings in Bands 4 and 5.
Weather observation and prediction also are major applications of multi-
spectral imaging from satellites.For example,Fig.1.11is an image of Hurricane
Katrina one of the most devastating storms in recent memory in the Western
Hemisphere.This image was taken by a National Oceanographic and Atmos-
pheric Administration (NOAA) satellite using sensors in the visible and in-
frared bands.The eye of the hurricane is clearly visible in this image.
Figures 1.12and 1.13show an application of infrared imaging.These images
are part of the Nighttime Lights of the Worlddata set,which provides a global
inventory of human settlements.The images were generated by the infrared
imaging system mounted on a NOAA DMSP (Defense Meteorological Satel-
lite Program) satellite.The infrared imaging system operates in the band 10.0
to 13.4 (cid:2)m,and has the unique capability to observe faint sources of visible-
near infrared emissions present on the Earth’s surface,including cities,towns,
villages,gas flares,and fires.Even without formal training in image processing,it
is not difficult to imagine writing a computer program that would use these im-
ages to estimate the percent of total electrical energy used by various regions of
the world.
A major area of imaging in the visual spectrum is in automated visual in-
spection of manufactured goods.Figure 1.14shows some examples.Figure 1.14(a)
is a controller board for a CD-ROM drive.A typical image processing task
with products like this is to inspect them for missing parts (the black square on
the top,right quadrant of the image is an example of a missing component).</p>

<p>16 Chapter 1 ■ Introduction
FIGURE1.12
Infrared satellite
images of the
Americas.The
small gray map is
provided for
reference.
(Courtesy of
NOAA.)
Figure 1.14(b)is an imaged pill container.The objective here is to have a ma-
chine look for missing pills.Figure 1.14(c)shows an application in which image
processing is used to look for bottles that are not filled up to an acceptable
level.Figure 1.14(d)shows a clear-plastic part with an unacceptable number of
air pockets in it.Detecting anomalies like these is a major theme of industrial
inspection that includes other products such as wood and cloth.Figure 1.14(e)</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 17
FIGURE1.13
Infrared satellite
images of the
remaining
populated part of
the world.The
small gray map is
provided for
reference.
(Courtesy of
NOAA.)
shows a batch of cereal during inspection for color and the presence of anom-
alies such as burned flakes.Finally,Fig.1.14(f)shows an image of an intraocular
implant (replacement lens for the human eye).A “structured light”illumina-
tion technique was used to highlight for easier detection flat lens deformations
toward the center of the lens. The markings at 1 o’clock and 5 o’clock are
tweezer damage.Most of the other small speckle detail is debris.The objective
in this type of inspection is to find damaged or incorrectly manufactured im-
plants automatically,prior to packaging.
As a final illustration of image processing in the visual spectrum,consider
Fig.1.15.Figure 1.15(a) shows a thumb print.Images of fingerprints are rou-
tinely processed by computer,either to enhance them or to find features that
aid in the automated search of a database for potential matches.Figure 1.15(b)
shows an image of paper currency.Applications of digital image processing in
this area include automated counting and,in law enforcement,the reading of
the serial number for the purpose of tracking and identifying bills.The two ve-
hicle images shown in Figs.1.15(c) and (d) are examples of automated license
plate reading.The light rectangles indicate the area in which the imaging system</p>

<p>18 Chapter 1 ■ Introduction
a b
c d
e f
FIGURE1.14
Some examples
of manufactured
goods often
checked using
digital image
processing.
(a) A circuit
board controller.
(b) Packaged pills.
(c) Bottles.
(d) Air bubbles
in a clear-plastic
product.
(e) Cereal.
(f) Image of
intraocular
implant.
(Fig.(f) courtesy
of Mr.Pete Sites,
Perceptics
Corporation.)
detected the plate.The black rectangles show the results of automated reading
of the plate content by the system.License plate and other applications of char-
acter recognition are used extensively for traffic monitoring and surveillance.
1.3.5 Imaging in the Microwave Band
The dominant application of imaging in the microwave band is radar. The
unique feature of imaging radar is its ability to collect data over virtually any
region at any time,regardless of weather or ambient lighting conditions.Some</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 19
a b
c
d
FIGURE1.15
Some additional
examples of
imaging in the
visual spectrum.
(a) Thumb print.
(b) Paper
currency.(c) and
(d) Automated
license plate
reading.
(Figure (a)
courtesy of the
National Institute
of Standards and
Technology.
Figures (c) and
(d) courtesy of
Dr.Juan Herrera,
Perceptics
Corporation.)
radar waves can penetrate clouds,and under certain conditions can also see
through vegetation,ice,and dry sand.In many cases,radar is the only way to
explore inaccessible regions of the Earth’s surface.An imaging radar works
like a flash camera in that it provides its own illumination (microwave pulses)
to illuminate an area on the ground and take a snapshot image.Instead of a
camera lens,a radar uses an antenna and digital computer processing to record
its images.In a radar image,one can see only the microwave energy that was
reflected back toward the radar antenna.
Figure 1.16 shows a spaceborne radar image covering a rugged mountain-
ous area of southeast Tibet,about 90 km east of the city of Lhasa.In the lower
right corner is a wide valley of the Lhasa River,which is populated by Tibetan
farmers and yak herders and includes the village of Menba.Mountains in this
area reach about 5800 m (19,000 ft) above sea level,while the valley floors lie
about 4300 m (14,000 ft) above sea level. Note the clarity and detail of the
image,unencumbered by clouds or other atmospheric conditions that normally
interfere with images in the visual band.</p>

<p>20 Chapter 1 ■ Introduction
FIGURE1.16
Spaceborne radar
image of
mountains in
southeast Tibet.
(Courtesy of
NASA.)
1.3.6 Imaging in the Radio Band
As in the case of imaging at the other end of the spectrum (gamma rays),the
major applications of imaging in the radio band are in medicine and astronomy.
In medicine,radio waves are used in magnetic resonance imaging (MRI).This
technique places a patient in a powerful magnet and passes radio waves through
his or her body in short pulses.Each pulse causes a responding pulse of radio
waves to be emitted by the patient’s tissues.The location from which these sig-
nals originate and their strength are determined by a computer,which produces
a two-dimensional picture of a section of the patient.MRI can produce pictures
in any plane.Figure 1.17shows MRI images of a human knee and spine.
The last image to the right in Fig.1.18shows an image of the Crab Pulsar in
the radio band.Also shown for an interesting comparison are images of the
same region but taken in most of the bands discussed earlier.Note that each
image gives a totally different “view”of the Pulsar.
1.3.7 Examples in which Other Imaging Modalities Are Used
Although imaging in the electromagnetic spectrum is dominant by far,there
are a number of other imaging modalities that also are important.Specifically,
we discuss in this section acoustic imaging,electron microscopy,and synthetic
(computer-generated) imaging.
Imaging using “sound”finds application in geological exploration,industry,
and medicine.Geological applications use sound in the low end of the sound
spectrum (hundreds of Hz) while imaging in other areas use ultrasound (mil-
lions of Hz).The most important commercial applications of image processing
in geology are in mineral and oil exploration.For image acquisition over land,
one of the main approaches is to use a large truck and a large flat steel plate.
The plate is pressed on the ground by the truck, and the truck is vibrated
through a frequency spectrum up to 100 Hz.The strength and speed of the</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 21
a b
FIGURE1.17 MRI images of a human (a) knee,and (b) spine.(Image (a) courtesy of
Dr. Thomas R. Gest, Division of Anatomical Sciences, University of Michigan
Medical School,and (b) courtesy of Dr.David R.Pickens,Department of Radiology
and Radiological Sciences,Vanderbilt University Medical Center.)
returning sound waves are determined by the composition of the Earth below
the surface.These are analyzed by computer,and images are generated from
the resulting analysis.
For marine acquisition,the energy source consists usually of two air guns
towed behind a ship. Returning sound waves are detected by hydrophones
placed in cables that are either towed behind the ship,laid on the bottom of
the ocean, or hung from buoys (vertical cables).The two air guns are alter-
'
nately pressurized to 2000 psi and then set off.The constant motion of the
ship provides a transversal direction of motion that,together with the return-
ing sound waves, is used to generate a 3-D map of the composition of the
Earth below the bottom of the ocean.
Figure 1.19 shows a cross-sectional image of a well-known 3-D model
against which the performance of seismic imaging algorithms is tested.The
arrow points to a hydrocarbon (oil and/or gas) trap.This target is brighter than
the surrounding layers because the change in density in the target region is
Gamma X-ray Optical Infrared Radio
FIGURE1.18 Images of the Crab Pulsar (in the center of each image) covering the electromagnetic spectrum.
(Courtesy of NASA.)</p>

<p>22 Chapter 1 ■ Introduction
FIGURE1.19
Cross-sectional
image of a seismic
model.The arrow
points to a
hydrocarbon (oil
and/or gas) trap.
(Courtesy of
Dr.Curtis Ober,
Sandia National
Laboratories.)
larger.Seismic interpreters look for these “bright spots”to find oil and gas.The
layers above also are bright, but their brightness does not vary as strongly
across the layers.Many seismic reconstruction algorithms have difficulty imag-
ing this target because of the faults above it.
Although ultrasound imaging is used routinely in manufacturing,the best
known applications of this technique are in medicine,especially in obstetrics,
where unborn babies are imaged to determine the health of their develop-
ment.A byproduct of this examination is determining the sex of the baby.Ul-
trasound images are generated using the following basic procedure:
1. The ultrasound system (a computer, ultrasound probe consisting of a
source and receiver,and a display) transmits high-frequency (1 to 5 MHz)
sound pulses into the body.
2. The sound waves travel into the body and hit a boundary between tissues
(e.g., between fluid and soft tissue, soft tissue and bone). Some of the
sound waves are reflected back to the probe,while some travel on further
until they reach another boundary and get reflected.
3. The reflected waves are picked up by the probe and relayed to the com-
puter.
4. The machine calculates the distance from the probe to the tissue or organ
boundaries using the speed of sound in tissue (1540 m/s) and the time of
each echo’s return.
5. The system displays the distances and intensities of the echoes on the
screen,forming a two-dimensional image.
In a typical ultrasound image,millions of pulses and echoes are sent and re-
ceived each second.The probe can be moved along the surface of the body and
angled to obtain various views.Figure 1.20shows several examples.
We continue the discussion on imaging modalities with some examples of
electron microscopy.Electron microscopes function as their optical counter-
parts, except that they use a focused beam of electrons instead of light to
image a specimen.The operation of electron microscopes involves the follow-
ing basic steps:A stream of electrons is produced by an electron source and ac-
celerated toward the specimen using a positive electrical potential.This stream</p>

<p>1.3 ■ Examples of Fields that Use Digital Image Processing 23
a b
c d
FIGURE1.20
Examples of
ultrasound
imaging.(a) Baby.
(b) Another
view of baby.
(c) Thyroids.
(d) Muscle layers
showing lesion.
(Courtesy of
Siemens Medical
Systems,Inc.,
Ultrasound
Group.)
is confined and focused using metal apertures and magnetic lenses into a thin,
monochromatic beam.This beam is focused onto the sample using a magnetic
lens. Interactions occur inside the irradiated sample, affecting the electron
beam. These interactions and effects are detected and transformed into an
image,much in the same way that light is reflected from,or absorbed by,ob-
jects in a scene.These basic steps are carried out in all electron microscopes.
Atransmission electron microscope(TEM) works much like a slide projec-
tor.A projector shines (transmits) a beam of light through a slide;as the light
passes through the slide,it is modulated by the contents of the slide.This trans-
mitted beam is then projected onto the viewing screen,forming an enlarged
image of the slide.TEMs work the same way,except that they shine a beam of
electrons through a specimen (analogous to the slide). The fraction of the
beam transmitted through the specimen is projected onto a phosphor screen.
The interaction of the electrons with the phosphor produces light and,there-
fore,a viewable image.A scanning electron microscope (SEM),on the other
hand, actually scans the electron beam and records the interaction of beam
and sample at each location.This produces one dot on a phosphor screen.A
complete image is formed by a raster scan of the beam through the sample,
much like a TV camera.The electrons interact with a phosphor screen and
produce light. SEMs are suitable for “bulky” samples, while TEMs require
very thin samples.
Electron microscopes are capable of very high magnification.While light
microscopy is limited to magnifications on the order 1000*,electron microscopes</p>

<p>24 Chapter 1 ■ Introduction
a b
FIGURE1.21 (a) 250<em> SEM image of a tungsten filament following thermal failure
(note the shattered pieces on the lower left). (b) 2500</em> SEM image of damaged
integrated circuit. The white fibers are oxides resulting from thermal destruction.
(Figure (a) courtesy of Mr. Michael Shaffer, Department of Geological Sciences,
University of Oregon,Eugene;(b) courtesy of Dr.J.M.Hudak,McMaster University,
Hamilton,Ontario,Canada.)
can achieve magnification of 10,000* or more.Figure 1.21shows two SEM im-
ages of specimen failures due to thermal overload.
Weconclude the discussion of imaging modalities by looking briefly at im-
ages that are not obtained from physical objects.Instead,they are generated
by computer. Fractals are striking examples of computer-generated images
(Lu [1997]).Basically,a fractal is nothing more than an iterative reproduction
of a basic pattern according to some mathematical rules.For instance,tilingis
one of the simplest ways to generate a fractal image.A square can be subdi-
vided into four square subregions, each of which can be further subdivided
into four smaller square regions,and so on.Depending on the complexity of
the rules for filling each subsquare,some beautiful tile images can be generated
using this method.Of course,the geometry can be arbitrary.For instance,the
fractal image could be grown radially out of a center point. Figure 1.22(a)
shows a fractal grown in this way. Figure 1.22(b) shows another fractal (a
“moonscape”) that provides an interesting analogy to the images of space
used as illustrations in some of the preceding sections.
Fractal images tend toward artistic,mathematical formulations of “growth”
of subimage elements according to a set of rules.They are useful sometimes as
random textures.A more structured approach to image generation by computer
lies in 3-D modeling.This is an area that provides an important intersection
between image processing and computer graphics and is the basis for many
3-D visualization systems (e.g.,flight simulators).Figures 1.22(c)and (d)show
examples of computer-generated images.Since the original object is created in
3-D,images can be generated in any perspective from plane projections of the
3-D volume.Images of this type can be used for medical training and for a host
of other applications,such as criminal forensics and special effects.</p>

<p>1.4 ■ Fundamental Steps in Digital Image Processing 25
a b
c d
FIGURE1.22
(a) and (b) Fractal
images.(c) and
(d) Images
generated from
3-D computer
models of the
objects shown.
(Figures (a) and
(b) courtesy of
Ms.Melissa
D.Binde,
Swarthmore
College;(c) and
(d) courtesy of
NASA.)
1.4 Fundamental Steps in Digital Image Processing
It is helpful to divide the material covered in the following chapters into the
two broad categories defined in Section 1.1:methods whose input and output
are images,and methods whose inputs may be images but whose outputs are
attributes extracted from those images.This organization is summarized in
Fig.1.23.The diagram does not imply that every process is applied to an image.
Rather,the intention is to convey an idea of all the methodologies that can be
applied to images for different purposes and possibly with different objectives.
The discussion in this section may be viewed as a brief overview of the material
in the remainder of the book.
Image acquisitionis the first process in Fig.1.23.The discussion in Section 1.3
gave some hints regarding the origin of digital images.This topic is considered
in much more detail in Chapter 2,where we also introduce a number of basic
digital image concepts that are used throughout the book.Note that acquisi-
tion could be as simple as being given an image that is already in digital form.
Generally,the image acquisition stage involves preprocessing,such as scaling.
Image enhancementis the process of manipulating an image so that the re-
sult is more suitable than the original for a specific application. The word
specificis important here,because it establishes at the outset that enhancement
techniques are problem oriented.Thus,for example,a method that is quite use-
ful for enhancing X-ray images may not be the best approach for enhancing
satellite images taken in the infrared band of the electromagnetic spectrum.</p>

<p>26 Chapter 1 ■ Introduction
FIGURE1.23 Outputs of these processes generally are images
Fundamental
steps in digital
image processing. CHAPTER 6 CHAPTER 7 CHAPTER 8 CHAPTER 9
The chapter(s) Color image Wavelets and Morphological
indicated in the processing multiresolution Compression processing
boxes is where the processing
material
described in the
CHAPTER 5 CHAPTER 10
box is discussed.
Image
Segmentation
restoration
CHAPTERS 3 &amp; 4 CHAPTER 11
Image Knowledge base Representation
filtering and &amp; description
enhancement
CHAPTER 2 CHAPTER 12
Image Object
Problem
acquisition recognition
domain
There is no general “theory” of image enhancement.When an image is
processed for visual interpretation, the viewer is the ultimate judge of how
well a particular method works.Enhancement techniques are so varied,and
use so many different image processing approaches,that it is difficult to as-
semble a meaningful body of techniques suitable for enhancement in one
chapter without extensive background development.For this reason,and also
because beginners in the field of image processing generally find enhance-
ment applications visually appealing,interesting,and relatively simple to un-
derstand, we use image enhancement as examples when introducing new
concepts in parts of Chapter 2 and in Chapters 3 and 4.The material in the
latter two chapters span many of the methods used traditionally for image en-
hancement.Therefore,using examples from image enhancement to introduce
new image processing methods developed in these early chapters not only
saves having an extra chapter in the book dealing with image enhancement
but,more importantly,is an effective approach for introducing newcomers to
the details of processing techniques early in the book.However,as you will
see in progressing through the rest of the book, the material developed in
these chapters is applicable to a much broader class of problems than just
image enhancement.
Image restorationis an area that also deals with improving the appearance
of an image.However,unlike enhancement,which is subjective,image restora-
tion is objective,in the sense that restoration techniques tend to be based on
mathematical or probabilistic models of image degradation.Enhancement,on
the other hand,is based on human subjective preferences regarding what con-
stitutes a “good”enhancement result.
setubirtta
egami
era
yllareneg
sessecorp
eseht
fo
stuptuO</p>

<p>1.4 ■ Fundamental Steps in Digital Image Processing 27
Color image processingis an area that has been gaining in importance be-
cause of the significant increase in the use of digital images over the Internet.
Chapter 6covers a number of fundamental concepts in color models and basic
color processing in a digital domain.Color is used also in later chapters as the
basis for extracting features of interest in an image.
Wavelets are the foundation for representing images in various degrees of
resolution.In particular,this material is used in this book for image data com-
pression and for pyramidal representation, in which images are subdivided
successively into smaller regions.
Compression, as the name implies, deals with techniques for reducing the
storage required to save an image,or the bandwidth required to transmit it.Al-
though storage technology has improved significantly over the past decade,the
same cannot be said for transmission capacity.This is true particularly in uses of
the Internet, which are characterized by significant pictorial content. Image
compression is familiar (perhaps inadvertently) to most users of computers in
the form of image file extensions, such as the jpg file extension used in the
JPEG (Joint Photographic Experts Group) image compression standard.
Morphological processingdeals with tools for extracting image components
that are useful in the representation and description of shape.The material in
this chapter begins a transition from processes that output images to processes
that output image attributes,as indicated in Section 1.1.
Segmentation procedures partition an image into its constituent parts or
objects. In general, autonomous segmentation is one of the most difficult
tasks in digital image processing.A rugged segmentation procedure brings
the process a long way toward successful solution of imaging problems that
require objects to be identified individually.On the other hand,weak or er-
ratic segmentation algorithms almost always guarantee eventual failure. In
general,the more accurate the segmentation,the more likely recognition is
to succeed.
Representation and descriptionalmost always follow the output of a segmen-
tation stage,which usually is raw pixel data,constituting either the boundary of
a region (i.e.,the set of pixels separating one image region from another) or all
the points in the region itself.In either case,converting the data to a form suit-
able for computer processing is necessary.The first decision that must be made
is whether the data should be represented as a boundary or as a complete region.
Boundary representation is appropriate when the focus is on external shape
characteristics,such as corners and inflections.Regional representation is ap-
propriate when the focus is on internal properties,such as texture or skeletal
shape. In some applications, these representations complement each other.
Choosing a representation is only part of the solution for transforming raw
data into a form suitable for subsequent computer processing.A method must
also be specified for describing the data so that features of interest are high-
lighted.Description,also called feature selection,deals with extracting attributes
that result in some quantitative information of interest or are basic for differ-
entiating one class of objects from another.
Recognition is the process that assigns a label (e.g.,“vehicle”) to an object
based on its descriptors.As detailed in Section 1.1,we conclude our coverage of</p>

<p>28 Chapter 1 ■ Introduction
digital image processing with the development of methods for recognition of
individual objects.
So far we have said nothing about the need for prior knowledge or about the
interaction between the knowledge baseand the processing modules in Fig.1.23.
Knowledge about a problem domain is coded into an image processing system
in the form of a knowledge database.This knowledge may be as simple as de-
tailing regions of an image where the information of interest is known to be
located,thus limiting the search that has to be conducted in seeking that infor-
mation.The knowledge base also can be quite complex,such as an interrelated
list of all major possible defects in a materials inspection problem or an image
database containing high-resolution satellite images of a region in connection
with change-detection applications.In addition to guiding the operation of each
processing module,the knowledge base also controls the interaction between
modules.This distinction is made in Fig.1.23by the use of double-headed arrows
between the processing modules and the knowledge base,as opposed to single-
headed arrows linking the processing modules.
Although we do not discuss image display explicitly at this point,it is impor-
tant to keep in mind that viewing the results of image processing can take place
at the output of any stage in Fig.1.23.We also note that not all image process-
ing applications require the complexity of interactions implied by Fig.1.23.In
fact,not even all those modules are needed in many cases.For example,image
enhancement for human visual interpretation seldom requires use of any of the
other stages in Fig.1.23.In general,however,as the complexity of an image pro-
cessing task increases,so does the number of processes required to solve the
problem.
1.5 Components of an Image Processing System
As recently as the mid-1980s,numerous models of image processing systems
being sold throughout the world were rather substantial peripheral devices
that attached to equally substantial host computers. Late in the 1980s and
early in the 1990s, the market shifted to image processing hardware in the
form of single boards designed to be compatible with industry standard buses
and to fit into engineering workstation cabinets and personal computers. In
addition to lowering costs,this market shift also served as a catalyst for a sig-
nificant number of new companies specializing in the development of software
written specifically for image processing.
Although large-scale image processing systems still are being sold for mas-
sive imaging applications,such as processing of satellite images,the trend con-
tinues toward miniaturizing and blending of general-purpose small computers
with specialized image processing hardware.Figure 1.24shows the basic com-
ponents comprising a typical general-purpose system used for digital image
processing.The function of each component is discussed in the following para-
graphs,starting with image sensing.
With reference to sensing,two elements are required to acquire digital im-
ages.The first is a physical device that is sensitive to the energy radiated by the
object we wish to image.The second,called a digitizer,is a device for converting</p>

<p>1.5 ■ Components of an Image Processing System 29
Network FIGURE1.24
Components of a
general-purpose
image processing
system.
Image displays Computer Mass storage
Specialized
Image processing
Hardcopy image processing
software
hardware
Image sensors
Problem
domain
the output of the physical sensing device into digital form.For instance,in a
digital video camera,the sensors produce an electrical output proportional to
light intensity.The digitizer converts these outputs to digital data.These topics
are covered in Chapter 2.
Specialized image processing hardwareusually consists of the digitizer just
mentioned,plus hardware that performs other primitive operations,such as an
arithmetic logic unit (ALU),that performs arithmetic and logical operations
in parallel on entire images.One example of how an ALU is used is in averag-
ing images as quickly as they are digitized,for the purpose of noise reduction.
This type of hardware sometimes is called a front-end subsystem,and its most
distinguishing characteristic is speed.In other words,this unit performs func-
tions that require fast data throughputs (e.g., digitizing and averaging video
images at 30 frames/s) that the typical main computer cannot handle.
Thecomputerin an image processing system is a general-purpose computer
and can range from a PC to a supercomputer.In dedicated applications,some-
times custom computers are used to achieve a required level of performance,
but our interest here is on general-purpose image processing systems.In these
systems, almost any well-equipped PC-type machine is suitable for off-line
image processing tasks.
Softwarefor image processing consists of specialized modules that perform
specific tasks.A well-designed package also includes the capability for the user</p>

<p>30 Chapter 1 ■ Introduction
to write code that,as a minimum,utilizes the specialized modules.More so-
phisticated software packages allow the integration of those modules and
general-purpose software commands from at least one computer language.
Mass storage capability is a must in image processing applications. An
image of size 1024 * 1024pixels,in which the intensity of each pixel is an 8-bit
quantity, requires one megabyte of storage space if the image is not com-
pressed.When dealing with thousands,or even millions,of images,providing
adequate storage in an image processing system can be a challenge. Digital
storage for image processing applications falls into three principal categories:
(1) short-term storage for use during processing,(2) on-line storage for rela-
tively fast recall,and (3) archival storage,characterized by infrequent access.
Storage is measured in bytes (eight bits),Kbytes (one thousand bytes),Mbytes
(one million bytes),Gbytes (meaning giga,or one billion,bytes),and Tbytes
(meaning tera,or one trillion,bytes).
One method of providing short-term storage is computer memory.An-
other is by specialized boards,called frame buffers,that store one or more
images and can be accessed rapidly,usually at video rates (e.g.,at 30 com-
plete images per second).The latter method allows virtually instantaneous
image zoom, as well as scroll (vertical shifts) and pan (horizontal shifts).
Frame buffers usually are housed in the specialized image processing hard-
ware unit in Fig.1.24.On-line storage generally takes the form of magnetic
disks or optical-media storage.The key factor characterizing on-line storage
is frequent access to the stored data.Finally,archival storage is characterized
by massive storage requirements but infrequent need for access.Magnetic
tapes and optical disks housed in “jukeboxes”are the usual media for archival
applications.
Image displays in use today are mainly color (preferably flat screen) TV
monitors.Monitors are driven by the outputs of image and graphics display
cards that are an integral part of the computer system.Seldom are there re-
quirements for image display applications that cannot be met by display cards
available commercially as part of the computer system.In some cases,it is nec-
essary to have stereo displays,and these are implemented in the form of head-
gear containing two small displays embedded in goggles worn by the user.
Hardcopydevices for recording images include laser printers,film cameras,
heat-sensitive devices,inkjet units,and digital units,such as optical and CD-
ROM disks.Film provides the highest possible resolution,but paper is the ob-
vious medium of choice for written material. For presentations, images are
displayed on film transparencies or in a digital medium if image projection
equipment is used.The latter approach is gaining acceptance as the standard
for image presentations.
Networkingis almost a default function in any computer system in use today.
Because of the large amount of data inherent in image processing applications,
the key consideration in image transmission is bandwidth. In dedicated net-
works,this typically is not a problem,but communications with remote sites via
the Internet are not always as efficient.Fortunately,this situation is improving
quickly as a result of optical fiber and other broadband technologies.</p>

<p>■ References and Further Reading 31
Summary
The main purpose of the material presented in this chapter is to provide a sense of per-
spective about the origins of digital image processing and,more important,about cur-
rent and future areas of application of this technology.Although the coverage of these
topics in this chapter was necessarily incomplete due to space limitations, it should
have left you with a clear impression of the breadth and practical scope of digital image
processing.As we proceed in the following chapters with the development of image
processing theory and applications,numerous examples are provided to keep a clear
focus on the utility and promise of these techniques.Upon concluding the study of the
final chapter,a reader of this book will have arrived at a level of understanding that is
the foundation for most of the work currently underway in this field.
References and Further Reading
References at the end of later chapters address specific topics discussed in those
chapters,and are keyed to the Bibliography at the end of the book.However,in this
chapter we follow a different format in order to summarize in one place a body of
journals that publish material on image processing and related topics.We also pro-
vide a list of books from which the reader can readily develop a historical and current
perspective of activities in this field.Thus,the reference material cited in this chapter
is intended as a general-purpose,easily accessible guide to the published literature on
image processing.
Major refereed journals that publish articles on image processing and related topics
include:IEEE Transactions on Image Processing;IEEE Transactions on Pattern Analysis
and Machine Intelligence;Computer Vision,Graphics,and Image Processing (prior to
1991);Computer Vision and Image Understanding;IEEE Transactions on Systems,Man
and Cybernetics;Artificial Intelligence;Pattern Recognition;Pattern Recognition Letters;
Journal of the Optical Society of America(prior to 1984);Journal of the Optical Society
of America—A:Optics,Image Science and Vision;Optical Engineering;Applied Optics—
Information Processing;IEEE Transactions on Medical Imaging;Journal of Electronic
Imaging;IEEE Transactions on Information Theory;IEEE Transactions on Communi-
cations;IEEE Transactions on Acoustics,Speech and Signal Processing;Proceedings of
the IEEE;and issues of the IEEE Transactions on Computersprior to 1980.Publications
of the International Society for Optical Engineering (SPIE) also are of interest.
The following books, listed in reverse chronological order (with the number of
books being biased toward more recent publications),contain material that comple-
ments our treatment of digital image processing.These books represent an easily ac-
cessible overview of the area for the past 30-plus years and were selected to provide a
variety of treatments.They range from textbooks,which cover foundation material;to
handbooks,which give an overview of techniques;and finally to edited books,which
contain material representative of current research in the field.
Prince, J. L. and Links, J. M. [2006].Medical Imaging, Signals, and Systems, Prentice
Hall,Upper Saddle River,NJ.
Bezdek,J.C.et al.[2005].Fuzzy Models and Algorithms for Pattern Recognition and
Image Processing,Springer,New York.
Davies,E.R.[2005].Machine Vision:Theory,Algorithms,Practicalities,Morgan Kauf-
mann,San Francisco,CA.
Rangayyan,R.M.[2005].Biomedical Image Analysis,CRC Press,Boca Raton,FL.</p>

<p>32 Chapter 1 ■ Introduction
Umbaugh,S.E.[2005].Computer Imaging:Digital Image Analysis and Processing,CRC
Press,Boca Raton,FL.
Gonzalez,R.C.,Woods,R.E.,and Eddins,S.L.[2004].Digital Image Processing Using
MATLAB,Prentice Hall,Upper Saddle River,NJ.
Snyder,W. E. and Qi, Hairong [2004]. Machine Vision, Cambridge University Press,
New York.
Klette,R.and Rosenfeld,A.[2004].Digital Geometry—Geometric Methods for Digital
Picture Analysis,Morgan Kaufmann,San Francisco,CA.
Won,C.S.and Gray,R.M.[2004].Stochastic Image Processing,Kluwer Academic/Plenum
Publishers,New York.
Soille,P.[2003].Morphological Image Analysis:Principles and Applications,2nd ed.,
Springer-Verlag,New York.
Dougherty,E.R.and Lotufo,R.A.[2003].Hands-on Morphological Image Processing,
SPIE—The International Society for Optical Engineering,Bellingham,WA.
Gonzalez,R.C.and Woods,R.E.[2002].Digital Image Processing,2nd ed.,Prentice
Hall,Upper Saddle River,NJ.
Forsyth,D.F.and Ponce,J.[2002].Computer Vision—A Modern Approach,Prentice
Hall,Upper Saddle River,NJ.
Duda,R.O.,Hart,P.E.,and Stork,D.G.[2001].Pattern Classification,2nd ed.,John
Wiley &amp; Sons,New York.
Pratt,W.K.[2001].Digital Image Processing,3rd ed.,John Wiley &amp; Sons,New York.
Ritter, G. X. and Wilson, J. N. [2001]. Handbook of Computer Vision Algorithms in
Image Algebra,CRC Press,Boca Raton,FL.
Shapiro,L.G.and Stockman,G.C.[2001].Computer Vision,Prentice Hall,Upper Saddle
River,NJ.
Dougherty, E. R. (ed.) [2000]. Random Processes for Image and Signal Processing,
IEEE Press,New York.
Etienne,E.K.and Nachtegael,M.(eds.).[2000].Fuzzy Techniques in Image Processing,
Springer-Verlag,New York.
Goutsias,J.,Vincent,L.,and Bloomberg,D.S.(eds.).[2000].Mathematical Morphology
and Its Applications to Image and Signal Processing,Kluwer Academic Publishers,
Boston,MA.
Mallot,A.H.[2000].Computational Vision,The MIT Press,Cambridge,MA.
Marchand-Maillet,S.and Sharaiha,Y.M.[2000].Binary Digital Image Processing:A
Discrete Approach,Academic Press,New York.
Mitra,S.K.and Sicuranza,G.L.(eds.) [2000].Nonlinear Image Processing,Academic
Press,New York.
Edelman, S. [1999]. Representation and Recognition in Vision,The MIT Press, Cam-
bridge,MA.
Lillesand,T.M.and Kiefer,R.W.[1999].Remote Sensing and Image Interpretation,John
Wiley &amp; Sons,New York.
Mather,P.M.[1999].Computer Processing of Remotely Sensed Images:An Introduction,
John Wiley &amp; Sons,New York.
Petrou,M.and Bosdogianni,P.[1999].Image Processing:The Fundamentals,John Wiley
&amp; Sons,UK.
Russ,J.C.[1999].The Image Processing Handbook,3rd ed.,CRC Press,Boca Raton,FL.</p>

<p>■ References and Further Reading 33
Smirnov,A.[1999].Processing of Multidimensional Signals,Springer-Verlag,New York.
Sonka,M.,Hlavac,V.,and Boyle,R.[1999].Image Processing,Analysis,and Computer
Vision,PWS Publishing,New York.
Haskell,B.G.and Netravali,A.N.[1997].Digital Pictures:Representation,Compression,
and Standards,Perseus Publishing,New York.
Jahne,B.[1997].Digital Image Processing:Concepts,Algorithms,and Scientific Applica-
tions,Springer-Verlag,New York.
Castleman,K.R.[1996].Digital Image Processing,2nd ed.,Prentice Hall,Upper Saddle
River,NJ.
Geladi,P.and Grahn,H.[1996].Multivariate Image Analysis,John Wiley &amp; Sons,New York.
Bracewell,R.N.[1995].Two-Dimensional Imaging,Prentice Hall,Upper Saddle River,NJ.
Sid-Ahmed, M. A. [1995]. Image Processing: Theory, Algorithms, and Architectures,
McGraw-Hill,New York.
Jain,R.,Rangachar,K.,and Schunk,B.[1995].Computer Vision,McGraw-Hill,New York.
Mitiche,A.[1994].Computational Analysis of Visual Motion,Perseus Publishing,New York.
Baxes,G.A.[1994].Digital Image Processing:Principles and Applications,John Wiley
&amp; Sons,New York.
Gonzalez,R.C.and Woods,R.E.[1992].Digital Image Processing,Addison-Wesley,
Reading,MA.
Haralick,R.M.and Shapiro,L.G.[1992].Computer and Robot Vision,vols.1 &amp; 2,
Addison-Wesley,Reading,MA.
Pratt,W.K.[1991] Digital Image Processing,2nd ed.,Wiley-Interscience,New York.
Lim,J.S.[1990].Two-Dimensional Signal and Image Processing,Prentice Hall,Upper
Saddle River,NJ.
Jain,A. K. [1989]. Fundamentals of Digital Image Processing, Prentice Hall, Upper
Saddle River,NJ.
Schalkoff,R.J.[1989].Digital Image Processing and Computer Vision,John Wiley &amp;
Sons,New York.
Giardina,C.R.and Dougherty,E.R.[1988].Morphological Methods in Image and Signal
Processing,Prentice Hall,Upper Saddle River,NJ.
Levine,M.D.[1985].Vision in Man and Machine,McGraw-Hill,New York.
Serra,J.[1982].Image Analysis and Mathematical Morphology,Academic Press,New
York.
Ballard,D.H.and Brown,C.M.[1982].Computer Vision,Prentice Hall,Upper Saddle
River,NJ.
Fu,K.S.[1982].Syntactic Pattern Recognition and Applications,Prentice Hall,Upper
Saddle River,NJ.
Nevatia,R.[1982].Machine Perception,Prentice Hall,Upper Saddle River,NJ.
Pavlidis,T.[1982].Algorithms for Graphics and Image Processing,Computer Science
Press,Rockville,MD.
Rosenfeld,A.and Kak,A.C.[1982].Digital Picture Processing,2nd ed.,vols.1 &amp; 2,
Academic Press,New York.
Hall,E.L.[1979].Computer Image Processing and Recognition,Academic Press,New York.
Gonzalez,R.C.and Thomason,M.G.[1978].Syntactic Pattern Recognition:An Intro-
duction,Addison-Wesley,Reading,MA.</p>

<p>34 Chapter 1 ■ Introduction
Andrews,H.C.and Hunt,B.R.[1977].Digital Image Restoration,Prentice Hall,Upper
Saddle River,NJ.
Pavlidis,T.[1977].Structural Pattern Recognition,Springer-Verlag,New York.
Tou,J.T.and Gonzalez,R.C.[1974].Pattern Recognition Principles,Addison-Wesley,
Reading,MA.
Andrews, H. C. [1970]. Computer Techniques in Image Processing,Academic Press,
New York.</p>

<p>2
Digital Image
Fundamentals
Those who wish to succeed must ask the right
preliminary questions.
Aristotle
Preview
The purpose of this chapter is to introduce you to a number of basic concepts
in digital image processing that are used throughout the book.Section 2.1
summarizes the mechanics of the human visual system,including image for-
mation in the eye and its capabilities for brightness adaptation and discrimi-
nation.Section 2.2 discusses light,other components of the electromagnetic
spectrum, and their imaging characteristics. Section 2.3 discusses imaging
sensors and how they are used to generate digital images.Section 2.4intro-
duces the concepts of uniform image sampling and intensity quantization.
Additional topics discussed in that section include digital image representa-
tion,the effects of varying the number of samples and intensity levels in an
image,the concepts of spatial and intensity resolution,and the principles of
image interpolation. Section 2.5 deals with a variety of basic relationships
between pixels.Finally,Section 2.6is an introduction to the principal math-
ematical tools we use throughout the book.A second objective of that sec-
tion is to help you begin developing a “feel”for how these tools are used in
a variety of basic image processing tasks.The scope of these tools and their
application are expanded as needed in the remainder of the book.
35</p>

<p>36 Chapter 2 ■ Digital Image Fundamentals
2.1 Elements of Visual Perception
Although the field of digital image processing is built on a foundation of math-
ematical and probabilistic formulations,human intuition and analysis play a
central role in the choice of one technique versus another, and this choice
often is made based on subjective,visual judgments.Hence,developing a basic
understanding of human visual perception as a first step in our journey
through this book is appropriate. Given the complexity and breadth of this
topic,we can only aspire to cover the most rudimentary aspects of human vi-
sion.In particular,our interest is in the mechanics and parameters related to
how images are formed and perceived by humans.We are interested in learn-
ing the physical limitations of human vision in terms of factors that also are
used in our work with digital images.Thus, factors such as how human and
electronic imaging devices compare in terms of resolution and ability to adapt
to changes in illumination are not only interesting, they also are important
from a practical point of view.
2.1.1 Structure of the Human Eye
Figure 2.1 shows a simplified horizontal cross section of the human eye.The
eye is nearly a sphere, with an average diameter of approximately 20 mm.
Three membranes enclose the eye: the cornea and sclera outer cover; the
choroid;and the retina.The cornea is a tough,transparent tissue that covers
FIGURE2.1 Cornea
Simplified
Iris
diagram of a cross
section of the dy
human eye. bo Anterior chamber Ciliary muscle
Ciliary
Lens
Ciliary fibers
Visual axis
Vitreous humor
Retina
Blind spot
Fovea
Sclera
Choroid
Nerve
&amp; sheath</p>

<p>2.1 ■ Elements of Visual Perception 37
the anterior surface of the eye.Continuous with the cornea,the sclera is an
opaque membrane that encloses the remainder of the optic globe.
The choroid lies directly below the sclera.This membrane contains a net-
work of blood vessels that serve as the major source of nutrition to the eye.
Even superficial injury to the choroid,often not deemed serious,can lead to
severe eye damage as a result of inflammation that restricts blood flow.The
choroid coat is heavily pigmented and hence helps to reduce the amount of ex-
traneous light entering the eye and the backscatter within the optic globe.At
its anterior extreme,the choroid is divided into the ciliary body and the iris.
The latter contracts or expands to control the amount of light that enters the
eye.The central opening of the iris (the pupil) varies in diameter from approx-
imately 2 to 8 mm.The front of the iris contains the visible pigment of the eye,
whereas the back contains a black pigment.
Thelensis made up of concentric layers of fibrous cells and is suspended by
fibers that attach to the ciliary body.It contains 60 to 70%water,about 6%fat,
and more protein than any other tissue in the eye.The lens is colored by a
slightly yellow pigmentation that increases with age.In extreme cases,exces-
sive clouding of the lens, caused by the affliction commonly referred to as
cataracts, can lead to poor color discrimination and loss of clear vision.The
lens absorbs approximately 8% of the visible light spectrum, with relatively
higher absorption at shorter wavelengths.Both infrared and ultraviolet light
are absorbed appreciably by proteins within the lens structure and,in exces-
sive amounts,can damage the eye.
The innermost membrane of the eye is the retina,which lines the inside of
the wall’s entire posterior portion. When the eye is properly focused, light
from an object outside the eye is imaged on the retina.Pattern vision is afford-
ed by the distribution of discrete light receptors over the surface of the retina.
There are two classes of receptors:conesandrods.The cones in each eye num-
ber between 6 and 7 million.They are located primarily in the central portion
of the retina,called the fovea,and are highly sensitive to color.Humans can re-
solve fine details with these cones largely because each one is connected to its
own nerve end.Muscles controlling the eye rotate the eyeball until the image
of an object of interest falls on the fovea. Cone vision is called photopic or
bright-light vision.
The number of rods is much larger:Some 75 to 150 million are distributed
over the retinal surface.The larger area of distribution and the fact that sever-
al rods are connected to a single nerve end reduce the amount of detail dis-
cernible by these receptors.Rods serve to give a general,overall picture of the
field of view.They are not involved in color vision and are sensitive to low lev-
els of illumination.For example,objects that appear brightly colored in day-
light when seen by moonlight appear as colorless forms because only the rods
are stimulated.This phenomenon is known as scotopicor dim-light vision.
Figure 2.2 shows the density of rods and cones for a cross section of the
right eye passing through the region of emergence of the optic nerve from the
eye.The absence of receptors in this area results in the so-called blind spot(see
Fig.2.1).Except for this region,the distribution of receptors is radially sym-
metric about the fovea. Receptor density is measured in degrees from the</p>

<p>38 Chapter 2 ■ Digital Image Fundamentals
FIGURE2.2 180,000
Distribution of
Blind spot
rods and cones in Cones
Rods
the retina.
135,000
90,000
45,000
80(cid:3) 60(cid:3) 40(cid:3) 20(cid:3) 0(cid:3) 20(cid:3) 40(cid:3) 60(cid:3) 80(cid:3)
Degrees from visual axis (center of fovea)
fovea (that is,in degrees off axis,as measured by the angle formed by the visu-
al axis and a line passing through the center of the lens and intersecting the
retina).Note in Fig.2.2that cones are most dense in the center of the retina (in
the center area of the fovea).Note also that rods increase in density from the
center out to approximately 20°off axis and then decrease in density out to the
extreme periphery of the retina.
The fovea itself is a circular indentation in the retina of about 1.5 mm in di-
ameter.However,in terms of future discussions,talking about square or rec-
tangular arrays of sensing elements is more useful. Thus, by taking some
liberty in interpretation,we can view the fovea as a square sensor array of size
1.5 mm * 1.5 mm.The density of cones in that area of the retina is approxi-
mately 150,000 elements per mm2.Based on these approximations,the number
of cones in the region of highest acuity in the eye is about 337,000 elements.
Just in terms of raw resolving power,a charge-coupled device (CCD) imaging
chip of medium resolution can have this number of elements in a receptor
array no larger than 5 mm * 5 mm.While the ability of humans to integrate
intelligence and experience with vision makes these types of number compar-
isons somewhat superficial,keep in mind for future discussions that the basic
ability of the eye to resolve detail certainly is comparable to current electronic
imaging sensors.
2.1.2 Image Formation in the Eye
In an ordinary photographic camera,the lens has a fixed focal length,and fo-
cusing at various distances is achieved by varying the distance between the
lens and the imaging plane,where the film (or imaging chip in the case of a
digital camera) is located.In the human eye,the converse is true;the distance
between the lens and the imaging region (the retina) is fixed, and the focal
length needed to achieve proper focus is obtained by varying the shape of the
lens.The fibers in the ciliary body accomplish this,flattening or thickening the
2mm
rep
senoc
ro
sdor
fo
.oN</p>

<p>2.1 ■ Elements of Visual Perception 39
FIGURE2.3
Graphical
representation of
C
the eye looking at
15 m
a palm tree.Point
Cis the optical
center of the lens.
100 m 17 mm
lens for distant or near objects,respectively.The distance between the center
of the lens and the retina along the visual axis is approximately 17 mm.The
range of focal lengths is approximately 14 mm to 17 mm, the latter taking
place when the eye is relaxed and focused at distances greater than about 3 m.
The geometry in Fig. 2.3 illustrates how to obtain the dimensions of an
image formed on the retina.For example,suppose that a person is looking at a
tree 15 m high at a distance of 100 m.Letting hdenote the height of that object
in the retinal image, the geometry of Fig. 2.3 yields 15&gt;100 = h&gt;17 or
h = 2.55 mm.As indicated in Section 2.1.1,the retinal image is focused pri-
marily on the region of the fovea.Perception then takes place by the relative
excitation of light receptors,which transform radiant energy into electrical im-
pulses that ultimately are decoded by the brain.
2.1.3 Brightness Adaptation and Discrimination
Because digital images are displayed as a discrete set of intensities,the eye’s
ability to discriminate between different intensity levels is an important consid-
eration in presenting image processing results.The range of light intensity levels
to which the human visual system can adapt is enormous—on the order of 1010—
from the scotopic threshold to the glare limit.Experimental evidence indicates
thatsubjective brightness(intensity as perceivedby the human visual system) is a
logarithmic function of the light intensity incident on the eye.Figure 2.4,a plot
FIGURE2.4
Glare limit
Range of
subjective
brightness
sensations
showing a
particular
B
a adaptation level.
B
b
Scotopic
Scotopic Photopic
threshold
(cid:1)6 (cid:1)4 (cid:1)2 0 2 4
Log of intensity (mL)
ssenthgirb
evitcejbuS
egnar
noitatpadA</p>

<p>40 Chapter 2 ■ Digital Image Fundamentals
of light intensity versus subjective brightness,illustrates this characteristic.The
long solid curve represents the range of intensities to which the visual system
can adapt.In photopic vision alone,the range is about 106.The transition from
scotopic to photopic vision is gradual over the approximate range from 0.001
to 0.1 millilambert (-3 to -1 mL in the log scale),as the double branches of
the adaptation curve in this range show.
The essential point in interpreting the impressive dynamic range depicted in
Fig.2.4is that the visual system cannot operate over such a range simultaneously.
Rather,it accomplishes this large variation by changing its overall sensitivity,a
phenomenon known as brightness adaptation.The total range of distinct inten-
sity levels the eye can discriminate simultaneously is rather small when com-
pared with the total adaptation range. For any given set of conditions, the
current sensitivity level of the visual system is called the brightness adaptation
level, which may correspond, for example, to brightness B in Fig. 2.4. The
a
short intersecting curve represents the range of subjective brightness that the
eye can perceive when adapted to this level.This range is rather restricted,
having a level B at and below which all stimuli are perceived as indistinguish-
b
able blacks.The upper portion of the curve is not actually restricted but,if ex-
tended too far,loses its meaning because much higher intensities would simply
raise the adaptation level higher than B .
a
The ability of the eye to discriminate between changes in light intensity at
any specific adaptation level is also of considerable interest.A classic experi-
ment used to determine the capability of the human visual system for bright-
ness discrimination consists of having a subject look at a flat, uniformly
illuminated area large enough to occupy the entire field of view.This area typ-
ically is a diffuser,such as opaque glass,that is illuminated from behind by a
light source whose intensity,I,can be varied.To this field is added an incre-
ment of illumination,¢I,in the form of a short-duration flash that appears as
a circle in the center of the uniformly illuminated field,as Fig.2.5shows.
If ¢Iis not bright enough,the subject says “no,”indicating no perceivable
change.As ¢Igets stronger,the subject may give a positive response of “yes,”in-
dicating a perceived change.Finally,when ¢I is strong enough,the subject will
give a response of “yes”all the time.The quantity ¢I &gt;I,where ¢I is the incre-
c c
ment of illumination discriminable 50%of the time with background illumination
I,is called the Weber ratio.A small value of ¢I &gt;Imeans that a small percentage
c
change in intensity is discriminable.This represents “good”brightness discrimi-
nation.Conversely,a large value of ¢I &gt;Imeans that a large percentage change
c
in intensity is required.This represents “poor”brightness discrimination.
FIGURE2.5 Basic
experimental
setup used to I(cid:4)(cid:5)I
characterize
brightness
discrimination.
I</p>

<p>2.1 ■ Elements of Visual Perception 41
1.0 FIGURE2.6
Typical Weber
0.5 ratio as a function
of intensity.
0
(cid:1)0.5
(cid:1)1.0
(cid:1)1.5
(cid:1)2.0
(cid:1)4 (cid:1)3 (cid:1)2 (cid:1)1 0 1 2 3 4
logI
A plot of log¢I &gt;I as a function of log I has the general shape shown in
c
Fig. 2.6.This curve shows that brightness discrimination is poor (the Weber
ratio is large) at low levels of illumination,and it improves significantly (the
Weber ratio decreases) as background illumination increases.The two branch-
es in the curve reflect the fact that at low levels of illumination vision is carried
out by the rods,whereas at high levels (showing better discrimination) vision is
the function of cones.
If the background illumination is held constant and the intensity of the
other source, instead of flashing, is now allowed to vary incrementally from
never being perceived to always being perceived,the typical observer can dis-
cern a total of one to two dozen different intensity changes.Roughly,this re-
sult is related to the number of different intensities a person can see at any one
point in a monochrome image.This result does not mean that an image can be
represented by such a small number of intensity values because, as the eye
roams about the image, the average background changes, thus allowing a
different set of incremental changes to be detected at each new adaptation
level.The net consequence is that the eye is capable of a much broader range
ofoverallintensity discrimination.In fact,we show in Section 2.4.3that the eye
is capable of detecting objectionable contouring effects in monochrome im-
ages whose overall intensity is represented by fewer than approximately two
dozen levels.
Two phenomena clearly demonstrate that perceived brightness is not a
simple function of intensity.The first is based on the fact that the visual sys-
tem tends to undershoot or overshoot around the boundary of regions of dif-
ferent intensities.Figure 2.7(a)shows a striking example of this phenomenon.
Although the intensity of the stripes is constant,we actually perceive a bright-
ness pattern that is strongly scalloped near the boundaries [Fig.2.7(c)].These
seemingly scalloped bands are called Mach bandsafter Ernst Mach,who first
described the phenomenon in 1865.
The second phenomenon,called simultaneous contrast,is related to the fact
that a region’s perceived brightness does not depend simply on its intensity,as
Fig.2.8 demonstrates.All the center squares have exactly the same intensity.
I/I(cid:5)gol
c</p>

<p>42 Chapter 2 ■ Digital Image Fundamentals
a
b
c
FIGURE2.7
Illustration of the
Mach band effect.
Perceived
intensity is not a
simple function of
Actual intensity
actual intensity.
Perceived intensity
However, they appear to the eye to become darker as the background gets
lighter.A more familiar example is a piece of paper that seems white when
lying on a desk,but can appear totally black when used to shield the eyes while
looking directly at a bright sky.
Other examples of human perception phenomena are optical illusions, in
which the eye fills in nonexisting information or wrongly perceives geometri-
cal properties of objects.Figure 2.9 shows some examples.In Fig.2.9(a),the
outline of a square is seen clearly,despite the fact that no lines defining such a
figure are part of the image.The same effect,this time with a circle,can be seen
in Fig.2.9(b);note how just a few lines are sufficient to give the illusion of a
a b c
FIGURE2.8 Examples of simultaneous contrast.All the inner squares have the same
intensity,but they appear progressively darker as the background becomes lighter.</p>

<p>2.2 ■ Light and the Electromagnetic Spectrum 43
a b
c d
FIGURE2.9 Some
well-known
optical illusions.
complete circle.The two horizontal line segments in Fig.2.9(c)are of the same
length,but one appears shorter than the other.Finally,all lines in Fig.2.9(d)that
are oriented at 45°are equidistant and parallel.Yet the crosshatching creates the
illusion that those lines are far from being parallel.Optical illusions are a char-
acteristic of the human visual system that is not fully understood.
2.2 Light and the Electromagnetic Spectrum
The electromagnetic spectrum was introduced in Section 1.3.We now consider
this topic in more detail.In 1666,Sir Isaac Newton discovered that when a beam
of sunlight is passed through a glass prism,the emerging beam of light is not
white but consists instead of a continuous spectrum of colors ranging from violet
at one end to red at the other.As Fig.2.10shows,the range of colors we perceive
in visible light represents a very small portion of the electromagnetic spectrum.
On one end of the spectrum are radio waves with wavelengths billions of times
longer than those of visible light.On the other end of the spectrum are gamma
rays with wavelengths millions of times smaller than those of visible light.The
electromagnetic spectrum can be expressed in terms of wavelength,frequency,
or energy.Wavelength (l)and frequency (n)are related by the expression
c
l = (2.2-1)
n</p>

<p>44 Chapter 2 ■ Digital Image Fundamentals
Energy of one photon (electron volts)
106 105 104 103 102 101 1 10(cid:1)1 10(cid:1)2 10(cid:1)3 10(cid:1)4 10(cid:1)5 10(cid:1)6 10(cid:1)7 10(cid:1)8 10(cid:1)9
Frequency (Hz)
1021 1020 1019 1018 1017 1016 1015 1014 1013 1012 1011 1010 109 108 107 106 105
Wavelength (meters)
10(cid:1)12 10(cid:1)11 10(cid:1)10 10(cid:1)9 10(cid:1)8 10(cid:1)7 10(cid:1)6 10(cid:1)5 10(cid:1)4 10(cid:1)3 10(cid:1)2 10(cid:1)1 1 101 102 103
Gamma rays X-rays Ultraviolet Infrared Microwaves Radio waves
Visible spectrum
0.4(cid:6) 10(cid:1)6 0.5(cid:6) 10(cid:1)6 0.6(cid:6) 10(cid:1)6 0.7(cid:6) 10(cid:1)6
Ultraviolet Violet Blue Green Yellow Orange Red Infrared
FIGURE2.10 The electromagnetic spectrum.The visible spectrum is shown zoomed to facilitate explanation,
but note that the visible spectrum is a rather narrow portion of the EM spectrum.
wherecis the speed of light (2.998 * 108 m&gt;s).The energy of the various com-
ponents of the electromagnetic spectrum is given by the expression
E = hn (2.2-2)
wherehis Planck’s constant.The units of wavelength are meters,with the terms
microns(denoted (cid:2)m and equal to 10-6 m) and nanometers (denoted nm and
equal to
10-9
m)being used just as frequently.Frequency is measured in Hertz
(Hz),with one Hertz being equal to one cycle of a sinusoidal wave per second.
A commonly used unit of energy is the electron-volt.
Electromagnetic waves can be visualized as propagating sinusoidal waves
with wavelength l(Fig.2.11),or they can be thought of as a stream of massless
particles,each traveling in a wavelike pattern and moving at the speed of light.
Each massless particle contains a certain amount (or bundle) of energy.Each
FIGURE2.11 l
Graphical
representation of
one wavelength.</p>

<p>2.2 ■ Light and the Electromagnetic Spectrum 45
bundle of energy is called a photon.We see from Eq. (2.2-2) that energy is
proportional to frequency,so the higher-frequency (shorter wavelength) elec-
tromagnetic phenomena carry more energy per photon. Thus, radio waves
have photons with low energies, microwaves have more energy than radio
waves,infrared still more,then visible,ultraviolet,X-rays,and finally gamma
rays,the most energetic of all.This is the reason why gamma rays are so dan-
gerous to living organisms.
Light is a particular type of electromagnetic radiation that can be sensed by
the human eye.The visible (color) spectrum is shown expanded in Fig.2.10for
the purpose of discussion (we consider color in much more detail in Chapter 6).
The visible band of the electromagnetic spectrum spans the range from approxi-
mately 0.43(cid:2)m(violet) to about 0.79(cid:2)m(red).For convenience,the color spec-
trum is divided into six broad regions:violet,blue,green,yellow,orange,and red.
No color (or other component of the electromagnetic spectrum) ends abruptly,
but rather each range blends smoothly into the next,as shown in Fig.2.10.
The colors that humans perceive in an object are determined by the nature
of the light reflectedfrom the object.A body that reflects light relatively bal-
anced in all visible wavelengths appears white to the observer. However, a
body that favors reflectance in a limited range of the visible spectrum exhibits
some shades of color.For example,green objects reflect light with wavelengths
primarily in the 500 to 570 nm range while absorbing most of the energy at
other wavelengths.
Light that is void of color is called monochromatic (or achromatic) light.
The only attribute of monochromatic light is its intensityor amount.Because
the intensity of monochromatic light is perceived to vary from black to grays
and finally to white, the term gray level is used commonly to denote mono-
chromatic intensity.We use the terms intensityandgray levelinterchangeably
in subsequent discussions.The range of measured values of monochromatic
light from black to white is usually called the gray scale,and monochromatic
images are frequently referred to as gray-scale images.
Chromatic (color) light spans the electromagnetic energy spectrum from
approximately 0.43 to 0.79(cid:2)m, as noted previously.In addition to frequency,
three basic quantities are used to describe the quality of a chromatic light
source: radiance, luminance, and brightness.Radiance is the total amount of
energy that flows from the light source, and it is usually measured in watts
(W).Luminance,measured in lumens (lm),gives a measure of the amount of
energy an observer perceives from a light source.For example,light emitted
from a source operating in the far infrared region of the spectrum could have
significant energy (radiance),but an observer would hardly perceive it;its lu-
minance would be almost zero.Finally,as discussed in Section 2.1,brightnessis
a subjective descriptor of light perception that is practically impossible to
measure.It embodies the achromatic notion of intensity and is one of the key
factors in describing color sensation.
Continuing with the discussion of Fig. 2.10, we note that at the short-
wavelength end of the electromagnetic spectrum,we have gamma rays and
X-rays.As discussed in Section 1.3.1,gamma radiation is important for medical
and astronomical imaging,and for imaging radiation in nuclear environments.</p>

<p>46 Chapter 2 ■ Digital Image Fundamentals
Hard (high-energy) X-rays are used in industrial applications. Chest and
dental X-rays are in the lower energy (soft) end of the X-ray band.The soft
X-ray band transitions into the far ultraviolet light region, which in turn
blends with the visible spectrum at longer wavelengths.Moving still higher in
wavelength,we encounter the infrared band,which radiates heat,a fact that
makes it useful in imaging applications that rely on “heat signatures.”The part
of the infrared band close to the visible spectrum is called the near-infraredre-
gion.The opposite end of this band is called the far-infraredregion.This latter
region blends with the microwave band.This band is well known as the source
of energy in microwave ovens,but it has many other uses,including communi-
cation and radar.Finally,the radio wave band encompasses television as well
as AM and FM radio.In the higher energies,radio signals emanating from cer-
tain stellar bodies are useful in astronomical observations.Examples of images
inmostof the bands just discussed are given in Section 1.3.
In principle,if a sensor can be developed that is capable of detecting energy
radiated by a band of the electromagnetic spectrum,we can image events of
interest in that band.It is important to note,however,that the wavelength of
an electromagnetic wave required to “see”an object must be of the same size
as or smaller than the object.For example,a water molecule has a diameter on
the order of
10-10
m.Thus,to study molecules,we would need a source capable
of emitting in the far ultraviolet or soft X-ray region.This limitation, along
with the physical properties of the sensor material,establishes the fundamen-
tal limits on the capability of imaging sensors, such as visible, infrared, and
other sensors in use today.
Although imaging is based predominantly on energy radiated by electro-
magnetic waves, this is not the only method for image generation. For ex-
ample, as discussed in Section 1.3.7, sound reflected from objects can be
used to form ultrasonic images. Other major sources of digital images are
electron beams for electron microscopy and synthetic images used in graphics
and visualization.
2.3 Image Sensing and Acquisition
Most of the images in which we are interested are generated by the combina-
tion of an “illumination” source and the reflection or absorption of energy
from that source by the elements of the “scene” being imaged.We enclose
illuminationandscenein quotes to emphasize the fact that they are consider-
ably more general than the familiar situation in which a visible light source il-
luminates a common everyday 3-D (three-dimensional) scene. For example,
the illumination may originate from a source of electromagnetic energy such
as radar, infrared, or X-ray system. But, as noted earlier, it could originate
from less traditional sources,such as ultrasound or even a computer-generated
illumination pattern. Similarly, the scene elements could be familiar objects,
but they can just as easily be molecules,buried rock formations,or a human
brain.Depending on the nature of the source,illumination energy is reflected
from,or transmitted through,objects.An example in the first category is light</p>

<p>2.3 ■ Image Sensing and Acquisition 47
reflected from a planar surface.An example in the second category is when
X-rays pass through a patient’s body for the purpose of generating a diagnos-
tic X-ray film.In some applications,the reflected or transmitted energy is fo-
cused onto a photoconverter (e.g., a phosphor screen), which converts the
energy into visible light.Electron microscopy and some applications of gamma
imaging use this approach.
Figure 2.12 shows the three principal sensor arrangements used to trans-
form illumination energy into digital images.The idea is simple:Incoming en-
ergy is transformed into a voltage by the combination of input electrical power
and sensor material that is responsive to the particular type of energy being
detected.The output voltage waveform is the response of the sensor(s),and a
digital quantity is obtained from each sensor by digitizing its response.In this
section,we look at the principal modalities for image sensing and generation.
Image digitizing is discussed in Section 2.4.
Energy a
b
Filter c
FIGURE2.12
(a) Single imaging
Sensing material
Power in sensor.
(b) Line sensor.
(c) Array sensor.
Voltage waveform out
Housing</p>

<p>48 Chapter 2 ■ Digital Image Fundamentals
FIGURE2.13 Film
Combining a
single sensor with
motion to
generate a 2-D Rotation
Sensor
image.
Linear motion
One image line out
per increment of rotation
and full linear displacement
of sensor from left to right
2.3.1 Image Acquisition Using a Single Sensor
Figure 2.12(a)shows the components of a single sensor.Perhaps the most fa-
miliar sensor of this type is the photodiode,which is constructed of silicon ma-
terials and whose output voltage waveform is proportional to light.The use of
a filter in front of a sensor improves selectivity.For example,a green (pass) fil-
ter in front of a light sensor favors light in the green band of the color spec-
trum.As a consequence,the sensor output will be stronger for green light than
for other components in the visible spectrum.
In order to generate a 2-D image using a single sensor,there has to be rela-
tive displacements in both the x- and y-directions between the sensor and the
area to be imaged.Figure 2.13 shows an arrangement used in high-precision
scanning,where a film negative is mounted onto a drum whose mechanical ro-
tation provides displacement in one dimension.The single sensor is mounted
on a lead screw that provides motion in the perpendicular direction.Because
mechanical motion can be controlled with high precision,this method is an in-
expensive (but slow) way to obtain high-resolution images.Other similar me-
chanical arrangements use a flat bed, with the sensor moving in two linear
directions.These types of mechanical digitizers sometimes are referred to as
microdensitometers.
Another example of imaging with a single sensor places a laser source coin-
cident with the sensor.Moving mirrors are used to control the outgoing beam
in a scanning pattern and to direct the reflected laser signal onto the sensor.
This arrangement can be used also to acquire images using strip and array sen-
sors,which are discussed in the following two sections.
2.3.2 Image Acquisition Using Sensor Strips
A geometry that is used much more frequently than single sensors consists of an
in-line arrangement of sensors in the form of a sensor strip,as Fig.2.12(b)shows.
The strip provides imaging elements in one direction.Motion perpendicular to the
strip provides imaging in the other direction,as shown in Fig.2.14(a).This is the
type of arrangement used in most flat bed scanners.Sensing devices with 4000 or
more in-line sensors are possible.In-line sensors are used routinely in airborne
imaging applications,in which the imaging system is mounted on an aircraft that</p>

<p>2.3 ■ Image Sensing and Acquisition 49
One image line out per
increment of linear motion
Imaged area
Image
reconstruction
Cross-sectional images
Linear motion of 3-D object
Sensor strip
3-D object
X-ray source
Lin e ar
m
otio n
Sensor ring
a b
FIGURE2.14 (a) Image acquisition using a linear sensor strip.(b) Image acquisition using a circular sensor strip.
flies at a constant altitude and speed over the geographical area to be imaged.
One-dimensional imaging sensor strips that respond to various bands of the
electromagnetic spectrum are mounted perpendicular to the direction of
flight.The imaging strip gives one line of an image at a time,and the motion of
the strip completes the other dimension of a two-dimensional image.Lenses
or other focusing schemes are used to project the area to be scanned onto the
sensors.
Sensor strips mounted in a ring configuration are used in medical and in-
dustrial imaging to obtain cross-sectional (“slice”) images of 3-D objects, as
Fig.2.14(b)shows.A rotating X-ray source provides illumination and the sen-
sors opposite the source collect the X-ray energy that passes through the ob-
ject (the sensors obviously have to be sensitive to X-ray energy).This is the
basis for medical and industrial computerized axial tomography (CAT) imag-
ing as indicated in Sections 1.2and 1.3.2.It is important to note that the output
of the sensors must be processed by reconstruction algorithms whose objective
is to transform the sensed data into meaningful cross-sectional images (see
Section 5.11).In other words,images are not obtained directly from the sen-
sors by motion alone;they require extensive processing.A 3-D digital volume
consisting of stacked images is generated as the object is moved in a direction</p>

<p>50 Chapter 2 ■ Digital Image Fundamentals
perpendicular to the sensor ring. Other modalities of imaging based on the
CAT principle include magnetic resonance imaging (MRI) and positron emis-
sion tomography (PET).The illumination sources,sensors,and types of images
are different,but conceptually they are very similar to the basic imaging ap-
proach shown in Fig.2.14(b).
2.3.3 Image Acquisition Using Sensor Arrays
Figure 2.12(c)shows individual sensors arranged in the form of a 2-D array.
Numerous electromagnetic and some ultrasonic sensing devices frequently
are arranged in an array format.This is also the predominant arrangement
found in digital cameras.A typical sensor for these cameras is a CCD array,
which can be manufactured with a broad range of sensing properties and can
be packaged in rugged arrays of 4000 * 4000 elements or more.CCD sen-
sors are used widely in digital cameras and other light sensing instruments.
The response of each sensor is proportional to the integral of the light ener-
gy projected onto the surface of the sensor,a property that is used in astro-
nomical and other applications requiring low noise images.Noise reduction
is achieved by letting the sensor integrate the input light signal over minutes
or even hours.Because the sensor array in Fig.2.12(c)is two-dimensional,its
key advantage is that a complete image can be obtained by focusing the en-
ergy pattern onto the surface of the array.Motion obviously is not necessary,
as is the case with the sensor arrangements discussed in the preceding two
sections.
The principal manner in which array sensors are used is shown in Fig.2.15.
In some cases,we image This figure shows the energy from an illumination source being reflected
the source directly,as in
from a scene element (as mentioned at the beginning of this section,the en-
obtaining images of the
sun. ergy also could be transmitted through the scene elements).The first function
performed by the imaging system in Fig. 2.15(c) is to collect the incoming
energy and focus it onto an image plane.If the illumination is light,the front
end of the imaging system is an optical lens that projects the viewed scene
onto the lens focal plane, as Fig. 2.15(d) shows.The sensor array, which is
Image intensities can coincident with the focal plane,produces outputs proportional to the integral
become negative during
of the light received at each sensor.Digital and analog circuitry sweep these
processing or as a result
of interpretation.For outputs and convert them to an analog signal,which is then digitized by an-
example,in radar images
other section of the imaging system.The output is a digital image,as shown
objects moving toward a
radar system often are diagrammatically in Fig.2.15(e).Conversion of an image into digital form is
interpreted as having
the topic of Section 2.4.
negative velocities while
objects moving away are
interpreted as having
positive velocities.Thus,a 2.3.4 ASimple Image Formation Model
velocity image might be
coded as having both As introduced in Section 1.1, we denote images by two-dimensional func-
positive and negative
values.When storing and tions of the form f(x,y).The value or amplitude of f at spatial coordinates
displaying images,we (x,y) is a positive scalar quantity whose physical meaning is determined by
normally scale the inten-
sities so that the smallest the source of the image.When an image is generated from a physical process,
negative value becomes 0 its intensity values are proportional to energy radiated by a physical source
(see Section 2.6.3regard-
ing intensity scaling). (e.g., electromagnetic waves). As a consequence, f(x,y) must be nonzero</p>

<p>2.3 ■ Image Sensing and Acquisition 51
Illumination (energy)
source
Output (digitized) image
Imaging system
(Internal) image plane
Scene element
a
c d e
b
FIGURE2.15 An example of the digital image acquisition process.(a) Energy (“illumination”) source.(b) An
element of a scene.(c) Imaging system.(d) Projection of the scene onto the image plane.(e) Digitized image.
and finite;that is,
0 6 f(x,y) 6 q (2.3-1)
The function f(x,y)may be characterized by two components:(1) the amount
of source illumination incident on the scene being viewed,and (2) the amount of il-
lumination reflected by the objects in the scene.Appropriately,these are called the
illuminationandreflectancecomponents and are denoted by i(x,y)and r(x,y),
respectively.The two functions combine as a product to form f(x,y):
f(x,y) = i(x,y)r(x,y) (2.3-2)
where
0 6 i(x,y) 6 q (2.3-3)
and
0 6 r(x,y) 6 1 (2.3-4)
Equation (2.3-4) indicates that reflectance is bounded by 0 (total absorption)
and 1 (total reflectance).The nature of i(x,y) is determined by the illumina-
tion source,and r(x,y)is determined by the characteristics of the imaged ob-
jects.It is noted that these expressions also are applicable to images formed
via transmission of the illumination through a medium,such as a chest X-ray.</p>

<p>52 Chapter 2 ■ Digital Image Fundamentals
In this case,we would deal with a transmissivity instead of a reflectivity func-
tion,but the limits would be the same as in Eq.(2.3-4),and the image function
formed would be modeled as the product in Eq.(2.3-2).
■
EXAMPLE 2.1: The values given in Eqs.(2.3-3) and (2.3-4) are theoretical bounds.The fol-
Some typical lowing average numerical figures illustrate some typical ranges of i(x,y) for
values of visible light.On a clear day,the sun may produce in excess of 90,000 lm&gt;m2
illumination and
of illumination on the surface of the Earth.This figure decreases to less than
reflectance.
10,000 lm&gt;m2 on a cloudy day.On a clear evening,a full moon yields about
0.1 lm&gt;m2of illumination.The typical illumination level in a commercial office
is about 1000 lm&gt;m2.Similarly,the following are typical values of r(x,y):0.01
for black velvet,0.65 for stainless steel,0.80 for flat-white wall paint,0.90 for
silver-plated metal,and 0.93 for snow. ■
Let the intensity (gray level) of a monochrome image at any coordinates
(x ,y )be denoted by
0 0
/ = f(x ,y ) (2.3-5)
0 0
From Eqs.(2.3-2) through (2.3-4),it is evident that /lies in the range
L … / … L (2.3-6)
min max
In theory,the only requirement on L is that it be positive,and on L that
min max
it be finite.In practice,L = i r and L = i r . Using the pre-
min min min max max max
ceding average office illumination and range of reflectance values as guide-
lines,we may expect L L 10and L L 1000to be typical limits for indoor
min max
values in the absence of additional illumination.
The interval [L ,L ] is called the gray (or intensity) scale. Common
min max
practice is to shift this interval numerically to the interval [0,L - 1], where
/ = 0is considered black and / = L - 1is considered white on the gray scale.
All intermediate values are shades of gray varying from black to white.
2.4 Image Sampling and Quantization
The discussion of From the discussion in the preceding section,we see that there are numerous
sampling in this section is ways to acquire images,but our objective in all is the same:to generate digital
of an intuitive nature.We
consider this topic in images from sensed data.The output of most sensors is a continuous voltage
depth in Chapter 4. waveform whose amplitude and spatial behavior are related to the physical
phenomenon being sensed.To create a digital image,we need to convert the
continuous sensed data into digital form.This involves two processes:sampling
andquantization.
2.4.1 Basic Concepts in Sampling and Quantization
The basic idea behind sampling and quantization is illustrated in Fig. 2.16.
Figure 2.16(a)shows a continuous image fthat we want to convert to digital
form.An image may be continuous with respect to the x- and y-coordinates,
and also in amplitude.To convert it to digital form, we have to sample the</p>

<p>2.4 ■ Image Sampling and Quantization 53
a b
c d
A B FIGURE2.16
Generating a
digital image.
(a) Continuous
image.(b) A scan
line from AtoB
A B in the continuous
image,used to
illustrate the
concepts of
sampling and
quantization.
(c) Sampling and
quantization.
A B A B
(d) Digital
scan line.
Sampling
function in both coordinates and in amplitude.Digitizing the coordinate values
is called sampling.Digitizing the amplitude values is called quantization.
The one-dimensional function in Fig.2.16(b)is a plot of amplitude (intensity
level) values of the continuous image along the line segment ABin Fig.2.16(a).
The random variations are due to image noise.To sample this function,we take
equally spaced samples along line AB,as shown in Fig.2.16(c).The spatial loca-
tion of each sample is indicated by a vertical tick mark in the bottom part of the
figure.The samples are shown as small white squares superimposed on the func-
tion.The set of these discrete locations gives the sampled function.However,the
values of the samples still span (vertically) a continuous range of intensity val-
ues.In order to form a digital function,the intensity values also must be con-
verted (quantized) into discrete quantities.The right side of Fig.2.16(c) shows
the intensity scale divided into eight discrete intervals, ranging from black to
white.The vertical tick marks indicate the specific value assigned to each of the
eight intensity intervals.The continuous intensity levels are quantized by assign-
ing one of the eight values to each sample.The assignment is made depending on
the vertical proximity of a sample to a vertical tick mark.The digital samples
resulting from both sampling and quantization are shown in Fig.2.16(d).Start-
ing at the top of the image and carrying out this procedure line by line produces
a two-dimensional digital image.It is implied in Fig.2.16that,in addition to the
number of discrete levels used,the accuracy achieved in quantization is highly
dependent on the noise content of the sampled signal.
Sampling in the manner just described assumes that we have a continuous
image in both coordinate directions as well as in amplitude. In practice, the
noitazitnauQ</p>

<p>54 Chapter 2 ■ Digital Image Fundamentals
method of sampling is determined by the sensor arrangement used to generate
the image.When an image is generated by a single sensing element combined
with mechanical motion,as in Fig.2.13,the output of the sensor is quantized in
the manner described above.However,spatial sampling is accomplished by se-
lecting the number of individual mechanical increments at which we activate
the sensor to collect data.Mechanical motion can be made very exact so,in
principle,there is almost no limit as to how fine we can sample an image using
this approach. In practice, limits on sampling accuracy are determined by
other factors,such as the quality of the optical components of the system.
When a sensing strip is used for image acquisition,the number of sensors in
the strip establishes the sampling limitations in one image direction.Mechani-
cal motion in the other direction can be controlled more accurately, but it
makes little sense to try to achieve sampling density in one direction that ex-
ceeds the sampling limits established by the number of sensors in the other.
Quantization of the sensor outputs completes the process of generating a dig-
ital image.
When a sensing array is used for image acquisition,there is no motion and
the number of sensors in the array establishes the limits of sampling in both di-
rections.Quantization of the sensor outputs is as before.Figure 2.17illustrates
this concept. Figure 2.17(a) shows a continuous image projected onto the
plane of an array sensor.Figure 2.17(b) shows the image after sampling and
quantization.Clearly,the quality of a digital image is determined to a large de-
gree by the number of samples and discrete intensity levels used in sampling
and quantization.However,as we show in Section 2.4.3,image content is also
an important consideration in choosing these parameters.
a b
FIGURE2.17 (a) Continuous image projected onto a sensor array.(b) Result of image
sampling and quantization.</p>

<p>2.4 ■ Image Sampling and Quantization 55
2.4.2 Representing Digital Images
Let f(s,t)represent a continuous image function of two continuous variables,
sandt.We convert this function into a digital imageby sampling and quanti-
zation, as explained in the previous section. Suppose that we sample the
continuous image into a 2-D array, f(x,y), containing M rows and N
columns, where (x,y) are discrete coordinates. For notational clarity and
convenience, we use integer values for these discrete coordinates:
x = 0, 1, 2,Á,M - 1 and y = 0, 1, 2,Á,N - 1. Thus, for example, the
value of the digital image at the origin is f(0, 0), and the next coordinate
value along the first row is f(0, 1).Here,the notation (0,1) is used to signify
the second sample along the first row.It does notmean that these are the val-
ues of the physical coordinates when the image was sampled.In general,the
value of the image at any coordinates (x,y)is denoted f(x,y),where xandy
are integers.The section of the real plane spanned by the coordinates of an
image is called the spatial domain,with x and y being referred to as spatial
variablesorspatial coordinates.
As Fig. 2.18 shows, there are three basic ways to represent f(x,y).
Figure2.18(a)is a plot of the function,with two axes determining spatial location
f(x, y) a
b c
FIGURE2.18
(a) Image plotted
as a surface.
(b) Image
displayed as a
visual intensity
array.
(c) Image shown
as a 2-D
y numerical array
(0,.5,and 1
x
represent black,
gray,and white,
Origin Origin respectively).
y 0 0 0 0 0 0 0(cid:2) (cid:2) (cid:2)0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
(cid:2)
0 0 0 0 (cid:2) 0 0 0 0
0 0 0 (cid:2) (cid:2).5.5.5 (cid:2) (cid:2) 0 0 0
0 0 0 .5.5 0 0 0
(cid:2)
(cid:2) .5 (cid:2) (cid:2) (cid:2)
(cid:2) (cid:2) 1 1 1(cid:2) (cid:2) (cid:2)
(cid:2) (cid:2)
1 1
(cid:2)
0 0 0 1 (cid:2) 0 0 0
(cid:2)
0 0 0 (cid:2) 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0(cid:2) (cid:2) (cid:2)0 0 0 0 0 0 0
x</p>

<p>56 Chapter 2 ■ Digital Image Fundamentals
and the third axis being the values of f(intensities) as a function of the two spa-
tial variables xandy.Although we can infer the structure of the image in this
example by looking at the plot,complex images generally are too detailed and
difficult to interpret from such plots.This representation is useful when work-
ing with gray-scale sets whose elements are expressed as triplets of the form
(x,y,z),wherexandyare spatial coordinates and zis the value of fat coordi-
nates (x,y).We work with this representation in Section 2.6.4.
The representation in Fig.2.18(b) is much more common.It shows f(x,y)
as it would appear on a monitor or photograph. Here, the intensity of each
point is proportional to the value of fat that point.In this figure,there are only
three equally spaced intensity values.If the intensity is normalized to the in-
terval [0,1],then each point in the image has the value 0,0.5,or 1.A monitor
or printer simply converts these three values to black,gray,or white,respec-
tively,as Fig.2.18(b) shows.The third representation is simply to display the
numerical values of f(x,y) as an array (matrix).In this example,f is of size
600 * 600elements,or 360,000 numbers.Clearly,printing the complete array
would be cumbersome and convey little information.When developing algo-
rithms, however, this representation is quite useful when only parts of the
image are printed and analyzed as numerical values. Figure 2.18(c) conveys
this concept graphically.
We conclude from the previous paragraph that the representations in
Figs.2.18(b) and (c) are the most useful.Image displays allow us to view re-
sults at a glance.Numerical arrays are used for processing and algorithm devel-
opment.In equation form,we write the representation of an M * Nnumerical
array as
f(0, 0) f(0, 1) Á f(0,N - 1)
f(1, 0) f(1, 1) Á f(1,N - 1)
f(x,y) = D T (2.4-1)
o o o
f(M - 1, 0) f(M - 1, 1) Á f(M - 1,N - 1)
Both sides of this equation are equivalent ways of expressing a digital image
quantitatively.The right side is a matrix of real numbers.Each element of this
matrix is called an image element, picture element, pixel, or pel. The terms
image and pixel are used throughout the book to denote a digital image and
its elements.
In some discussions it is advantageous to use a more traditional matrix no-
tation to denote a digital image and its elements:
a 0,0 a 0,1 Á a 0,N-1
A = D a 1,0 a 1,1 Á a 1,N-1 T (2.4-2)
o o o
a M-1,0 a M-1,1 Á a M-1,N-1</p>

<p>2.4 ■ Image Sampling and Quantization 57
Clearly,a = f(x = i,y = j) = f(i,j),so Eqs.(2.4-1) and (2.4-2) are identical
ij
matrices.We can even represent an image as a vector,v.For example,a column
vector of sizeMN * 1is formed by letting the first Melements of vbe the first
column of A,the next Melements be the second column,and so on.Alterna-
tively,we can use the rows instead of the columns of Ato form such a vector.
Either representation is valid,as long as we are consistent.
Returning briefly to Fig.2.18,note that the origin of a digital image is at the
top left,with the positive x-axis extending downward and the positive y-axis
extending to the right.This is a conventional representation based on the fact
that many image displays (e.g.,TV monitors) sweep an image starting at the
top left and moving to the right one row at a time.More important is the fact
that the first element of a matrix is by convention at the top left of the array,so
choosing the origin of f(x,y)at that point makes sense mathematically.Keep
in mind that this representation is the standard right-handed Cartesian coordi-
nate system with which you are familiar.†We simply show the axes pointing
downward and to the right,instead of to the right and up.
Expressing sampling and quantization in more formal mathematical terms
can be useful at times.Let Z and R denote the set of integers and the set of
real numbers,respectively.The sampling process may be viewed as partition-
ing the xy-plane into a grid,with the coordinates of the center of each cell in
the grid being a pair of elements from the Cartesian product Z2,which is the
set of all ordered pairs of elements (z,z),with z and z being integers from
i j i j
Z.Hence,f(x,y) is a digital image if (x,y) are integers from Z2 and f is a
function that assigns an intensity value (that is,a real number from the set
of real numbers,R) to each distinct pair of coordinates (x,y).This functional
assignment is the quantization process described earlier.If the intensity lev-
els also are integers (as usually is the case in this and subsequent chapters),
Z replaces R,and a digital image then becomes a 2-D function whose coor-
dinates and amplitude values are integers.
This digitization process requires that decisions be made regarding the val-
ues for M,N,and for the number,L,of discrete intensity levels.There are no
restrictions placed on M and N,other than they have to be positive integers.
However,due to storage and quantizing hardware considerations,the number
Often,it is useful for
of intensity levels typically is an integer power of 2:
computation or for
L = 2k (2.4-3) a pl ug ro pr oit sh em s t d oe sv ce al lo ep tm hee n Lt
intensity values to the
We assume that the discrete levels are equally spaced and that they are inte- range [0,1],in which case
gers in the interval [0,L - 1].Sometimes,the range of values spanned by the they cease to be integers.
However,in most cases
gray scale is referred to informally as the dynamic range.This is a term used in these values are scaled
back to the integer range
different ways in different fields.Here,we define the dynamic rangeof an imag-
[0,L-1]for image
ing system to be the ratio of the maximum measurable intensity to the minimum storage and display.
†Recall that a right-handed coordinate system is such that,when the index of the right hand points in the di-
rection of the positive x-axis and the middle finger points in the (perpendicular) direction of the positive
y-axis,the thumb points up.As Fig.2.18(a)shows,this indeed is the case in our image coordinate system.</p>

