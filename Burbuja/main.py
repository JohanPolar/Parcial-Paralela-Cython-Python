'''
Fecha 01 - Noviembre - 2022
Autor: Juan Camilo Rodriguez Fonseca
Materia: Parallel and Distributed Computing
Tema: Cython

La idea principal es exportar un '.csv' con la toma de tiempos
'''
import Burbuja_cy
import Burbuja_py
import time
import numpy as np


a = np.arange(1000)
array = np.random.choice(a, 1000, replace=False)
'''
Carga 1 
[59 48  0 98 90 28  9 70 93 80 24 52 35 29 73  8 91 36 18 61  3 32  2 88
 83 69 31 76 19  6 39 22 96 72 89 16 81 41 82 74  5 20 71 58 40 66 38 30
 27 45 97 49 63 99 75 51 44 17 77 14 68  7 12 11 64 86 56 57 65 60 13 95
 92 26 62 53 54 15 84 21  4 67 78 79 47 42 25 46 50  1 34 23 33 94 10 87
 55 85 37 43]
Carga 2 
[ 31 147 132 389 406 141 160 222  85 433 250 105 499 201 232 154 409  32
 259 353 188 213 179 328  23 238 436 307  80 193 114 483 491 468 210 355
 254 200  18 388 165 473 112 323 439  19  68 272 126 329 181 234 485  91
 339 214  21 317   3 237 206 350 332  71 470 221 495 441 122 359 462 187
 217  54 239 163  98 229 155 208  96 248 480 302 292  93 211 299 269 440
  22  63 305 338 130 109  83 392 218  46 458  34 111 104 243 390 138  20
 177 136 123 145 489 166  17 233 400 326 180  77 360 464 348 204 319 391
   9 120 186 263 445 340 335 463 419 189 230 372 481 300 397 277 262 346
 384 398 276 143 309 185 124 452 215  67  79 244   8  78 267 240 370 134
   4 106 108 393 194 417 312 121 415 354 146  24 364 113 101 336  82 446
 368 450 466 271  41 176 228  95 361 448 382 264 376 100  44 245 151 169
 330  52 296 407 320 431 209  36  73 161 199 274 103 418 241 385  56 293
  37 344  66 308  16  88 403  99 379 443  61 310 117 129  70  86 297 477
  12 380 438 424 288 265 471 404 174 324 311 128 337 321 118 260 426  28
 252 183 375  64 314 246 497 127  29 152 140 373 283  45  48 306 423  59
 125 381 207 266   2 249  84 168 474 456 226 451 365  13 366  33 313  40
 422  35 496 195 396 484  47 290 493 231 434 428 273 341 352  39 467 482
 421  94 270 150 173   7 158 476 453 191 197 119 460 345 116 184 405  49
  60 295 351 175  97 414 198  62 333 172 461 303 190 157 488 149 425 142
 159  74 411 395 298 399 487 444  92 402  90 479 427 412 131 301 437 356
 236  65 280 498 291 281 203 304 242 144 358 220  87 401 459 455 115 261
 367 475 322 490 192  42   0 363 225 435 212   1 486 492 135 253 416 387
 342 102 268  53 133 349 247 285 279 294 251 420  72 170 469 227 343 216
  76  26 282 413 258 315 316 278  58 287 386 167 383  38 275 162   6  69
 202  27 110 457 369 327 235 454 429  57 410 289  30  50  81 196  43 205
 449 171 494 148 255 107 432 378 331 472 164 182 377  51 347 465  15  89
 153 256 257 430 219 357 334 139 286 394 362  25 223 374 156 478 447  75
  14  10 224 178 318  55 137 371 442  11 325 284   5 408]


Carga 3 
[620 129 196 947 465 925 904 821 459 183  67 389 681 629 369 215  92 628
 609 984 337 657 816  77 263 214 124 430 234 773 217 450 862 703 765 336
  32 941 986 460  87 455 641 552 957 674 797 999  43 293 857 823 557 206
 996 875 278 757 811 404 762 451 575 777 507 461 274 497  66 296 501 741
 828 121 949 936 416 290 792 347 910 993  68 954 543 225 221 485 576 330
 145 872 586 359 350 247 116 581 778 466 358 599 896 529 479 437 937 931
 473  29 933 749 115 122 352 126 840 230 150 919  58 167 962 967 883 415
 668 638 318 745 746 370 574 244 232 960  12 677  88 393 216 555 137 888
  61 903 148 562 832   6 326 152 402 308 385 847 310 407 499 848 920 824
 476 441 540 956 771 787 526 711 690 973 176 805 338 645 906 119 809 763
 139 340 764 911 706 259 874 798 368 791 606 295 833 971  52 205 590 739
  65 836 365 750 197 730 312  56 538 707 236  59 998 727 228 632 133 608
 394  97 238 952 334 316 208 446  90 859 930 807 268 356 595 525 384 758
 484 504 190 243 734 864 625 946  27  41 104 261 735 992 398 630 170 220
 521  82  78 908 789 173 585 615 642 786 311 325 644 659 265 894 288 935
 180 834 258 880  44 871 588 432 291 248 959   7 736 650 157 179 804 869
 979 963 881 634 514 712 685 594 772 829 452 174 795 912 412 361 355  79
 309 870 718 550 417 493 678 423 546 191 332  85 475  69 924 399 406 646
 926 481 893 349  51   3 184  48 266  76  18  80 818 153 535 171 498 471
 651 696 300 426 981 776 424 458 929 846 492 689 456 582 968  91 201 583
  22 665 110 989 729 839 260 781 364 558 636 235 120  37 790 714 381 163
 731 323 939 271 532 202 109  10 994 118 785 719  17 655  50 878 335  35
 673  89 428 710 831 199 489 802 607   4  71 374 269 400 353 249 679 775
 624 547 983   2 767 500 944 351   1 744 503 568 289 480 250 990 343 882
 600 922 813 556 938 392 682 589 131 443 934 756 759  95  75 782 304 462
 670 203 597 808  54 769 613 909 692  73 825  81 548 580 927 661 528 972
 226 861 654 977 716 579 940 488  42 536 418 231   5 117 570 826  28 322
 616 298 210 591 853 486 495 713 970 988 515 738 709 403 754 510 844 753
 820  13 204 449 267 527 917 755 314 362  31 997 698 107  94 144 671 396
  57 380  23 161 164 519 855 587 251 331 177 907 141 253  63 256 837 702
 626 664  49 892 379 666  19 512 843 363 708 810 779 342 766 101 697 508
 160 737 270 155 578 980 760 474  38 303 732 545 172  21 419 554 567 966
 439 454 516 313 635 354 663 487 955 305 845 193  96 784 142 282  60 246
  15 969 375 111  25 687 478 889 704 102 382 279 618 464 621 273 386 241
 328 395 975 830 264 852 897 158  86 283 868 901 577 905 902  46 850 551
 637 147 517 453 951 224 317 513 987 542 932 564 675 218 748 943 559 496
  55 444 991 100  53 774 914 438 405 371 292 571 788 923 761 367  26 876
  33 566 344 149 324 420 377 284  34 879 448 733 958 431 827 240 835 865
 856 652 397 425 229 114 728 950 815 812 676 255 899  64 390 307 928 168
 895 125 252 414 200 411 410 592 803 948 945 285 468 409 726 561   9 483
 768 339 530  14 333 680 522 422 693 103 457 192 469 360 482 806 720 633
 700 541 136 887 688 799 974 502 128 123 898 649 434 166 207 262 433 272
 723 695 647 523 198 610 505 445 715 306 953 965 982 212 866 569 995 447
 401 105 302 985 254 388 239 822 108 185 181  98 838 188 534 531 222 639
 106 913 691 656 520 553 851 132 794  99 321 854 725 130 817 942 113  84
 849  47 281  40 372 436 209 135  93 842 159 245 421 413 653 643  24 345
 783 156 165 611 319 619 660 900 297 918 463  20 509 614 640  16   0 544
 740 886 860 127 961 877 612 648 227 112 801 622 346 699 237 722  39 563
 348 780 627 793 299 751 242 572 233 717 549 603  72 276 617  74 524 442
 146 275 211 427 280 391 884 743 686 491 182 800 533  83 315 518 537 631
 560  70 684   8 683 189 593 387 814 435 140 175 885 623 742  11 320 327
  36 472 978 429 598 573 440 494 669 604 301 186  62 701 915 964 921 470
 187 138  30 916 724 329 890 584 490 378 467 596  45 151 219 477 841 366
 747 873 511 667 863 213 383 662 286 294 373 721 341 223 277 178 605 357
 752 891 858 819 408 287 658 376 162 770 195 257 194 976 796 705 694 154
 506 601 169 565 539 134 143 602 867 672]

'''
print(array)
formato_datos = "{:.5f}, {:.5f}\n"

with open("burbuja3.csv","a") as archivo:
        archivo.write('Python,Cython\n')

for i in range(30):
	inicioPy=time.time()
	Burbuja_py.bubbleSort(array.tolist())
	finalPy=time.time()

	time_python = finalPy - inicioPy

	inicioCy=time.time()
	Burbuja_cy.bubbleSort(array.tolist())
	finalCy=time.time()

	time_cython = finalCy - inicioCy

	with open("burbuja3.csv","a") as archivo:
		archivo.write(formato_datos.format(time_python, time_cython))

    

#print("Tiempo de ejecucion con python: {}s\nTiempo de ejcucion con cython: {}s".format(time_python, time_cython))

#print("Cython es ",time_python/time_cython, " más rápido que python")










