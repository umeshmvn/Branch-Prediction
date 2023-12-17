import math
import sys

class treepred:
    def __init__(self):
        self.mpd = 0
        self.bvn = 0
        self.ib = 0
        self.pc_bits = 0
        self.ibg = 0
        self.bc = 0
        self.cb = 0
        self.fut = 0
        self.tee = []
        self.tree = []

    # In response to the branch's result, the pbb function modifies the current bit and handles mispredictions.
    def pbb(self, tee):
        if tee == "t":
            if self.cb < math.pow(2, int(self.ib) - 1):
                self.mpd += 1
            self.cb += 1
            if self.cb > self.bvn - 1:
                self.cb = self.bvn - 1
        elif tee == "n":
            if self.cb >= math.pow(2, int(self.ib) - 1):
                self.mpd += 1
            self.cb -= 1
            if self.cb < 0:
                self.cb = 0

    '''
    By using the pbb operation, the smith function initializes counters, 
    updates them in accordance with branch outcomes, and outputs where in it includes final counter value.
    '''
    def smith(self, s1, s2, s3):
        self.mpd = 0
        # N-bit value by performing a bitwise left shift
        self.bvn = 1 << self.ib
        # Current bit is allocated to N-bit value's leftmost bit.
        self.cb = 1 << (self.ib - 1)

        [self.pbb(tee) for tee in self.tee]

        print("COMMAND")
        print(f"./sim {s1} {s2} {s3}")
        print("OUTPUT")
        print("number of predictions:        ", len(self.tree))
        print("number of mispredictions:     ", self.mpd)
        misprediction_rate = (self.mpd / len(self.tree)) * 100 if len(self.tree) > 0 else 0
        print("misprediction rate:           ", f"{misprediction_rate:.2f}%")
        print("FINAL COUNTER CONTENT:        ", int(self.cb))
        return 0

    '''For guaranteing prediction values are inculcated within predetermined bounds, 
    the probibran function converts hexadecimal to binary, which indeed
    establishes the index, and simultaneously updates the prediction table based on the "tee" status'''
    def probibran(self, branch, tee, futble):
        treepc = bin(int(branch, 16))[2:]
        n = len(treepc)
        inf = int(treepc[n - int(self.ib) - 2:n - 2], 2)

        if tee == "t":
            if futble[inf] < 4:
                self.mpd += 1
            futble[inf] += 1
            if futble[inf] > 7:
                futble[inf] = 7
        elif tee == "n":
            if futble[inf] >= 4:
                self.mpd += 1
            futble[inf] -= 1
            if futble[inf] < 0:
                futble[inf] = 0
    '''
    Here bimodal function uses a prediction table to track branch results, 
    which indeed make changes to the table in response to the associated taken.
    '''
    def bimodal(self, s1, s2, s3):
        futble = [4] * (1 << self.ib)

        for branch, tee in zip(self.tree, self.tee):
            self.probibran(branch, tee, futble)

        print("COMMAND")
        print(f"./sim {s1} {s2} {s3}")
        print("OUTPUT")
        print("number of predictions:        ", len(self.tree))
        print("number of mispredictions:     ", self.mpd)
        misprediction_rate = (self.mpd / len(self.tree)) * 100 if len(self.tree) > 0 else 0
        print("misprediction rate:           ", f"{misprediction_rate:.2f}%")
        print("FINAL BIMODAL CONTENTS")
        for i in range(len(futble)):
            print(i, "    ", futble[i])
        return 0
    '''
    so, i combined binary representation with the global history reg and performing XOR operations, 
    the calif_inhh function calculates the branch and outputs a decimal number.
    '''
    def calif_inhh(self, branch, bvn, ib, hbgreg):
        gbhr = "".join(hbgreg)
        treepc = bin(int(branch, 16))[2:]
        n = len(treepc)

        vcp = treepc[n - bvn - 2: n - 2][bvn - ib:]
        desti = treepc[n - bvn - 2: n - 2][: bvn - ib]

        der = "".join(map(lambda x, y: "0" if x == y else "1", vcp, gbhr))
        return int(desti + der, 2)

    '''
    branch outcome and update_pred_and_gbh function tackles with updating of the history register, 
    the alteration of prediction table entries, and mispredictions. Also sees prediction values are constrained.
    '''
    def update_pred_and_gbh(self, tee, futble_cme, hbgreg, ib, mpd):
        if tee == "t":
            if futble_cme < 4:
                mpd += 1
            futble_cme += 1
            futble_cme = min(futble_cme, 7)
            hbgreg.insert(0, "1")
        elif tee == "n":
            if futble_cme >= 4:
                mpd += 1
            futble_cme -= 1
            futble_cme = max(futble_cme, 0)
            hbgreg.insert(0, "0")

        hbgreg.pop(ib)

        return mpd, futble_cme, hbgreg
    '''
    for getting branch outcomes, the gshare function makes use of a prediction table and a global history register, 
    updating the mispredictions, prediction table, and history reg.
    '''
    def gshare(self, s1, s2, s3, s4):
        futble = [4] * (1 << self.bvn)
        hbgreg = ['0'] * int(self.ib)
        mpd = 0

        for i, branch in enumerate(self.tree):
            inf = self.calif_inhh(branch, int(self.bvn), int(self.ib), hbgreg)
            mpd, futble[inf], hbgreg = self.update_pred_and_gbh(
                self.tee[i], futble[inf], hbgreg, int(self.ib), mpd
            )

        print("COMMAND")
        print(f"./sim {s1} {s2} {s3} {s4}")
        print("OUTPUT")
        print("number of predictions:        ", len(self.tree))
        print("number of mispredictions:     ", mpd)
        misprediction_rate = (mpd / len(self.tree)) * 100 if len(self.tree) > 0 else 0
        print("misprediction rate:           ", f"{misprediction_rate:.2f}%")
        print("FINAL GSHARE CONTENTS")
        for i in range(len(futble)):
            print(i, "   ", futble[i])
        return 0
    '''
    so to adjust prediction tables, history registers, 
    and mispredictions based on branch outcomes and predetermined criteria, the hybrid function combines bimodal and gshare predictors.
    '''
    def hybrid(self, s1, s2, s3, s4, s5, s6):
        global mpd
        mpd = 0
        bvn = 1 << self.ib
        futble_b = [4] * bvn

        futtable_g = [4] * (1 << self.pc_bits)

        hbgreg = ['0'] * self.ibg

        charu = [1] * (1 << self.bc)

        treee_length = len(self.tree)

        for i in range(treee_length):
            gbhr = "".join(hbgreg)
            treepc = bin(int(self.tree[i], 16))[2:]
            n = len(treepc)

            if treepc and n >= (int(self.bc) + 2):
                mixindx = int(treepc[n - int(self.bc) - 2: n - 2], 2)

                vcp = treepc[n - int(self.pc_bits) - 2: n - 2][int(self.pc_bits) - int(self.ibg):]
                desti = treepc[n - int(self.pc_bits) - 2: n - 2][: int(self.pc_bits) - int(self.ibg)]
                der = "".join(["0" if vcp[j] == gbhr[j] else "1" for j in range(int(self.ibg))])

                hem_kk = int(desti + der, 2)
                bb_l = int(treepc[n - int(self.ib) - 2: n - 2], 2)

                g = futtable_g[hem_kk]
                b = futble_b[bb_l]

                if self.tee[i] == "t":
                    if charu[mixindx] >= 2:
                        if futtable_g[hem_kk] < 4:
                            mpd += 1
                        futtable_g[hem_kk] += 1
                        if futtable_g[hem_kk] > 7:
                            futtable_g[hem_kk] = 7
                    elif charu[mixindx] < 2:
                        if futble_b[bb_l] < 4:
                            mpd += 1
                        futble_b[bb_l] += 1
                        if futble_b[bb_l] > 7:
                            futble_b[bb_l] = 7
                    hbgreg.insert(0, "1")
                    hbgreg.pop(int(self.ibg))

                    if b >= 4 and g < 4:
                        charu[mixindx] -= 1
                        if charu[mixindx] < 0:
                            charu[mixindx] = 0
                    elif b < 4 and g >= 4:
                        charu[mixindx] += 1
                        if charu[mixindx] > 3:
                            charu[mixindx] = 3
                elif self.tee[i] == "n":
                    if charu[mixindx] >= 2:
                        if futtable_g[hem_kk] >= 4:
                            mpd += 1
                        futtable_g[hem_kk] -= 1
                        if futtable_g[hem_kk] < 0:
                            futtable_g[hem_kk] = 0
                    elif charu[mixindx] < 2:
                        if futble_b[bb_l] >= 4:
                            mpd += 1
                        futble_b[bb_l] -= 1
                        if futble_b[bb_l] < 0:
                            futble_b[bb_l] = 0
                    hbgreg.insert(0, "0")
                    hbgreg.pop(int(self.ibg))

                    if b >= 4 and g < 4:
                        charu[mixindx] += 1
                        if charu[mixindx] > 3:
                            charu[mixindx] = 3
                    elif b < 4 and g >= 4:
                        charu[mixindx] -= 1
                        if charu[mixindx] < 0:
                            charu[mixindx] = 0

        print("COMMAND")
        print(f"./sim {s1} {s2} {s3} {s4} {s5} {s6}")
        print("OUTPUT")
        print("number of predictions:        ", treee_length)
        print("number of mispredictions:     ", mpd)
        print("misprediction rate:           ", f"{(mpd / treee_length) * 100:.2f}%")
        print("FINAL CHOOSER CONTENTS")
        for i in range(len(charu)):
            print(i, "   ", charu[i])
        print("FINAL GSHARE CONTENTS")
        for i in range(len(futtable_g)):
            print(i, "   ", futtable_g[i])
        print("FINAL BIMODAL CONTENTS")
        for i in range(len(futble_b)):
            print(i, "   ", futble_b[i])

        return 0

def main():
    knowfut = treepred()
    if sys.argv[1] == "smith":
        try:
            with open(sys.argv[3]) as f:
                for line in f:
                    bt = line.strip().split(" ")
                    knowfut.tee.append(bt[1])
                    knowfut.tree.append(bt[0])
        except Exception as e:
            print(e)

        knowfut.ib = int(sys.argv[2])
        knowfut.smith(sys.argv[1], sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "bimodal":
        try:
            with open(sys.argv[3]) as f:
                for line in f:
                    bt = line.strip().split(" ")
                    knowfut.tee.append(bt[1])
                    knowfut.tree.append(bt[0])
        except Exception as e:
            print(e)

        knowfut.ib = int(sys.argv[2])
        knowfut.bimodal(sys.argv[1], sys.argv[2], sys.argv[3])

    elif sys.argv[1] == "gshare":
        try:
            with open(sys.argv[4]) as f:
                for line in f:
                    bt = line.strip().split(" ")
                    knowfut.tee.append(bt[1])
                    knowfut.tree.append(bt[0])
        except Exception as e:
            print(e)

        knowfut.bvn = int(sys.argv[2])
        knowfut.ib = int(sys.argv[3])
        knowfut.gshare(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    elif sys.argv[1] == "hybrid":
        try:
            with open(sys.argv[6]) as f:
                for line in f:
                    bt = line.strip().split(" ")
                    knowfut.tee.append(bt[1])
                    knowfut.tree.append(bt[0])
        except Exception as e:
            print(e)

        knowfut.ib = int(sys.argv[5])
        knowfut.pc_bits = int(sys.argv[3])
        knowfut.ibg = int(sys.argv[4])
        knowfut.bc = int(sys.argv[2])
        knowfut.hybrid(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

if __name__ == "__main__":
    main()

