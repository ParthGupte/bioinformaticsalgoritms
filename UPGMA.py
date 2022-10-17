class Seq:
    def __init__(self,num,seq) -> None:
        self.num = num 
        self.seq = seq
    def dist(self,seq2):
        d = 0
        for i in range(seq2):
            if self.seq[i] != seq2[i]:
                d += 1
          
