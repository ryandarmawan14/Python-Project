import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)
video_capture.set(3, 640)
video_capture.set(4, 480)

KIRI = cv2.imread("imgarah_kiri.png")
KANAN = cv2.imread("imgarah_kanan.png")
LURUS = cv2.imread("imgarah_lurus.png")
STOP = cv2.imread("imgarah_stop.png")
ANGKA_1 = cv2.imread("imgbiner_1.png")
ANGKA_0 = cv2.imread("imgbiner_0.png")
BORDER3D = cv2.imread("imgborder.png")
HEADER3D = cv2.imread("imgheader.png")
FULLFRAME3D = cv2.imread("imgfullframe.png")
CROP3D = cv2.imread("imgcrop.png")
HASIL3D = cv2.imread("imghasil.png")
GRAYSCALE = cv2.imread("imggrayscale.png",flags=0)
BLUR = cv2.imread("imgblur.png",flags=0)
BORDER = cv2.imread("imgborder.png",flags=0)
HEADER = cv2.imread("imgheader.png",flags=0)
THRESHOLDING = cv2.imread("imgthresholding.png",flags=0)
BLOKBINER = cv2.imread("imgblokbiner.png",flags=0)

while (True):
    # Capture the frames
    ret, frame = video_capture.read(0)
    frame = cv2.flip(frame,flipCode=+1)
    # Crop the image by select
    A = frame[340:420, 0:80]
    B = frame[340:420, 80:160]
    C = frame[340:420, 160:240]
    D = frame[340:420, 240:320]
    E = frame[340:420, 320:400]
    F = frame[340:420, 400:480]
    G = frame[340:420, 480:560]
    H = frame[340:420, 560:640]
    POTONGAN = np.concatenate((A,B,C,D,E,F,G,H),axis=1)

    # Convert to grayscale
    gray = cv2.cvtColor(POTONGAN, cv2.COLOR_BGR2GRAY)

    # Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Color thresholding
    ACUAN = 255
    ret, thresh = cv2.threshold(blur, 90, ACUAN, cv2.THRESH_BINARY_INV)
    AN = thresh[0:80, 0:80]
    BN = thresh[0:80, 80:160]
    CN = thresh[0:80, 160:240]
    DN = thresh[0:80, 240:320]
    EN = thresh[0:80, 320:400]
    FN = thresh[0:80, 400:480]
    GN = thresh[0:80, 480:560]
    HN = thresh[0:80, 560:640]

    # seluruh isi array pada tiap blok pixel 80x80 dijumlahkan agar menjadi satu bilangan
    nilai_ambang=((80*80*ACUAN)/2)  #pembagi disini 50% sensitivity (tergantung pembagi)
    if AN.sum()  > nilai_ambang:
        BINER_A = 1
        BIN_A = ANGKA_1
    else:
        BINER_A = 0
        BIN_A = ANGKA_0
    if BN.sum()  > nilai_ambang:
        BINER_B = 1
        BIN_B = ANGKA_1
    else:
        BINER_B = 0
        BIN_B = ANGKA_0
    if CN.sum()  > nilai_ambang:
        BINER_C = 1
        BIN_C = ANGKA_1
    else:
        BINER_C = 0
        BIN_C = ANGKA_0
    if DN.sum()  > nilai_ambang:
        BINER_D = 1
        BIN_D = ANGKA_1
    else:
        BINER_D = 0
        BIN_D = ANGKA_0
    if EN.sum()  > nilai_ambang:
        BINER_E = 1
        BIN_E = ANGKA_1
    else:
        BINER_E = 0
        BIN_E = ANGKA_0
    if FN.sum()  > nilai_ambang:
        BINER_F = 1
        BIN_F = ANGKA_1
    else:
        BINER_F = 0
        BIN_F = ANGKA_0
    if GN.sum()  > nilai_ambang:
        BINER_G = 1
        BIN_G = ANGKA_1
    else:
        BINER_G = 0
        BIN_G = ANGKA_0
    if HN.sum()  > nilai_ambang:
        BINER_H = 1
        BIN_H = ANGKA_1
    else:
        BINER_H = 0
        BIN_H = ANGKA_0
    DATA_GPIO=(str('&')+str(BINER_A)+str(BINER_B)+str(BINER_C)+str(BINER_D)+str(BINER_E)+str(BINER_F)+str(BINER_G)+str(BINER_H))
    GAMBAR_BINER=np.concatenate((BIN_A,BIN_B,BIN_C,BIN_D,BIN_E,BIN_F,BIN_G,BIN_H),axis=1)


    # gerak maju jalan
    if DATA_GPIO == ('&00010000') or DATA_GPIO == ('&00100000') or DATA_GPIO == ('&00110000') or DATA_GPIO == ('&01000000') \
            or DATA_GPIO == ('&01010000') or DATA_GPIO == ('&01100000') or DATA_GPIO == ('&01110000') or DATA_GPIO == ('&10000000') \
            or DATA_GPIO == ('&10010000') or DATA_GPIO == ('&10100000') or DATA_GPIO == ('&10110000') or DATA_GPIO == ('&11000000') \
            or DATA_GPIO == ('&11010000') or DATA_GPIO == ('&11100000') or DATA_GPIO == ('&11110000'):
        KONDISI="BELOK KIRI"
        ARAH=KIRI
    elif DATA_GPIO == ('&00000001') or DATA_GPIO == ('&00000010') or DATA_GPIO == ('&00000011') or DATA_GPIO == ('&00000100') \
            or DATA_GPIO == ('&00000101') or DATA_GPIO == ('&00000110') or DATA_GPIO == ('&00000111') or DATA_GPIO == ('&00001000') \
            or DATA_GPIO == ('&00001001') or DATA_GPIO == ('&00001010') or DATA_GPIO == ('&00001011') or DATA_GPIO == ('&00001100')\
            or DATA_GPIO == ('&00001101') or DATA_GPIO == ('&00001110') or DATA_GPIO == ('&00001111'):
        KONDISI="BELOK KANAN"
        ARAH=KANAN
    elif DATA_GPIO == ("&00000000"):
        KONDISI="STOP"
        ARAH=STOP
    else:
        KONDISI="LURUS"
        ARAH=LURUS

    # visualisasi kotak biner
    KUBIK_1 = np.zeros((80,80))
    KUBIK_1[...] = [BINER_A]
    KUBIK_2 = np.zeros((80,80))
    KUBIK_2[...] = [BINER_B]
    KUBIK_3 = np.zeros((80,80))
    KUBIK_3[...] = [BINER_C]
    KUBIK_4 = np.zeros((80,80))
    KUBIK_4[...] = [BINER_D]
    KUBIK_5 = np.zeros((80,80))
    KUBIK_5[...] = [BINER_E]
    KUBIK_6 = np.zeros((80,80))
    KUBIK_6[...] = [BINER_F]
    KUBIK_7 = np.zeros((80,80))
    KUBIK_7[...] = [BINER_G]
    KUBIK_8 = np.zeros((80,80))
    KUBIK_8[...] = [BINER_H]
    AKHIR_BINER_BLOK = np.concatenate((KUBIK_1,KUBIK_2,KUBIK_3,KUBIK_4,KUBIK_5,KUBIK_6,KUBIK_7,KUBIK_8),axis=1)
    AKHIR = np.concatenate((GAMBAR_BINER, ARAH), axis=0)

    #visualisasi final
    VISUALISASI3D = np.concatenate((BORDER3D,HEADER3D,BORDER3D,FULLFRAME3D,frame,BORDER3D,CROP3D,POTONGAN,BORDER3D,HASIL3D,AKHIR,BORDER3D),axis=0)
    VISUALISASI2D_1 = np.concatenate((BORDER,HEADER,BORDER,GRAYSCALE,gray,BORDER,BLUR,blur,BORDER),axis=0)
    VISUALISASI2D_2 = np.concatenate((BORDER,HEADER,BORDER,THRESHOLDING,thresh,BORDER,BLOKBINER,AKHIR_BINER_BLOK,BORDER),axis=0)
    cv2.imshow("PSE-LINE FOLLOWER-JENDELA 1",VISUALISASI3D)
    cv2.imshow("PSE-LINE FOLLOWER-JENDELA 2",VISUALISASI2D_1)
    cv2.imshow("PSE-LINE FOLLOWER-JENDELA 3",VISUALISASI2D_2)

    # Hentikan paksa dengan tombol 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Keyboard Interupt")
        break