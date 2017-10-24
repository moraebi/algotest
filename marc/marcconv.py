class MarcFormat:

    def __init__(self):
        self.string=''

    def getString(self,s):
        self.string=s

    def interp(self):
        print('total bytes={}'.format(len(self.string)))
        print('Leader------------------------------------------------')
        print("Record Length={}".format(self.string[0:5]))
        print("Record Status={}".format(self.string[5:6]))
        print("Type of Record={}".format(self.string[6:7]))
        print("Biblio level={}".format(self.string[7:8]))
        print("Type of Ctrl={}".format(self.string[8:9]))
        print("Char coding scheme={}".format(self.string[9:10]))
        print("Indicator count={}".format(self.string[10:11]))
        print("Subfield code count={}".format(self.string[11:12]))
        print("Base address of data={}".format(self.string[12:17]))
        self.BaseAddr=int(self.string[12:17])
        print("Encoding level={}".format(self.string[17:18]))
        print("Descriptive cataloging form={}".format(self.string[18:19]))
        print("Multipart resource record level={}".format(self.string[19:20]))
        print("Length of the length-of-field={}".format(self.string[20:21]))
        print("Length of the starting-char-pos={}".format(self.string[21:22]))
        print("Length of the impl-defiend={}".format(self.string[22:23]))
        print("Undefined={}".format(self.string[23:24]))
        print("Directory---------------------------------------------")
        self.Dir=[]
        for i in range(24,self.BaseAddr-1,12):
            print("{} {} {} {}".format(i,self.string[i:i+3],self.string[i+3:i+7],self.string[i+7:i+12]))
            self.Dir.append([int(self.string[i:i+3]),int(self.string[i+3:i+7]),int(self.string[i+7:i+12])])
        for tag in self.Dir:
            s=str(self.string[self.BaseAddr+tag[2]:self.BaseAddr+tag[2]+tag[1]])
            print(tag[0],len(s))
            s=s.decode('utf-8')
            #print(tag[0],len(s),s)
            #print(tag[0],len(s.encode('euc-kr')),s.encode('euc-kr'))
    def ToEucKr(self):
        print('total bytes={}'.format(len(self.string_euckr)))
        print('Leader------------------------------------------------')
        print("Record Length={}".format(self.string_euckr[0:5]))
        print("Record Status={}".format(self.string_euckr[5:6]))
        print("Type of Record={}".format(self.string_euckr[6:7]))
        print("Biblio level={}".format(self.string_euckr[7:8]))
        print("Type of Ctrl={}".format(self.string_euckr[8:9]))
        print("Char coding scheme={}".format(self.string_euckr[9:10]))
        print("Indicator count={}".format(self.string_euckr[10:11]))
        print("Subfield code count={}".format(self.string_euckr[11:12]))
        print("Base address of data={}".format(self.string_euckr[12:17]))
        self.BaseAddr=int(self.string_euckr[12:17])
        print("Encoding level={}".format(self.string_euckr[17:18]))
        print("Descriptive cataloging form={}".format(self.string_euckr[18:19]))
        print("Multipart resource record level={}".format(self.string_euckr[19:20]))
        print("Length of the length-of-field={}".format(self.string_euckr[20:21]))
        print("Length of the starting-char-pos={}".format(self.string_euckr[21:22]))
        print("Length of the impl-defiend={}".format(self.string_euckr[22:23]))
        print("Undefined={}".format(self.string_euckr[23:24]))
        print("Directory---------------------------------------------")
        self.Dir=[]
        for i in range(24,self.BaseAddr-1,12):
            print("{} {} {} {}".format(i,self.string_euckr[i:i+3],self.string_euckr[i+3:i+7],self.string_euckr[i+7:i+12]))
            print("{} {} {}".format(self.Dir[],))
    def getFile(self,filename):
        file = open(filename, 'rb')
        self.string = file.readline()
        file.close()
        self.string_euckr=self.string.decode('utf-8').encode('euc-kr')
        file = open(filename+'euckr','wb')
        file.write(self.string_euckr)
        file.close()
        self.utf8_strs=self.string.split('\x1e')
        self.euckr_strs=self.string_euckr.split('\x1e')
        print(len(self.string),len(self.utf8_strs))
        print(self.utf8_strs)
        print(len(self.string_euckr),len(self.euckr_strs))
        print(self.euckr_strs)
        self.interp()
        self.ToEucKr()
if __name__ == '__main__':
    mf=MarcFormat()
    mf.getFile('BOOKINFO_MARC (9).TXT')
#    mf.getFile('20171007MARC.mrc')
