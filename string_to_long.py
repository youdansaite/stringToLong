class MasterClass:


    def longToString(self,inString):

    	tmp = list(inString)
    	#print tmp            # prints the charachter array

    	t = 0
    	for x in tmp:
    		t = t*10 + (ord(x)-48)   # Subtracting from ASCII value

        print type(t),t
        return t


    def test(self,inString):

    	if int(inString) == self.longToString(inString):
    		print "*******SUCCESS*******"
    	else:
    		print "____FAIL____"




b = MasterClass()

inp_num = raw_input("Enter number as STRING to conver to LONG = ")

b.test(inp_num) 