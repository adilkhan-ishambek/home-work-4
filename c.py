class Wordplay():
    def __init__(self,arr):
        self.arr = arr

    def words_with_length(self,n):
        output = []
        for i in self.arr:
            if len(i)==n:
                output.append(i)
        return output

    def starts_with(self,s):
        output = []
        for i in self.arr:
            if i[0]==s:
                output.append(i)
        return output

    def ends_with(self,s):
        output = []
        for i in self.arr:
            if i[-1]==s:
                output.append(i)
        return output

    def palindromes(self):
        output = []
        for i in self.arr:
            if i == i[::-1]:
                output.append(i)
        return output 

    def only(self,letters):
        output = []
        for i in self.arr:
            cnt = 0
            for j in i:
                if j in letters:
                    cnt+=1
            if len(i)==cnt:
                output.append(i)
        return output

    def avoids(self,letters):
        output = []
        for i in self.arr:
            cnt = 0
            for j in i:
                if j not in letters:
                    cnt+=1
            if len(i) == cnt:
                output.append(i)
        return output

g1 = Wordplay(["hesoyam","aezalmi","lol","heh","jumpjet","ohdude","baguvix","uzumymw","HelloWorld","rockketman"])

print(g1.words_with_length(7))
print(g1.starts_with("h"))
print(g1.ends_with("m"))
print(g1.palindromes())
print(g1.only("hesoyam"))
print(g1.avoids("as"))       