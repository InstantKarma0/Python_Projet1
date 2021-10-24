def formatedTime(i):
        """Return the time on a format MM:ss:cs from a int
        
        Keyword Arguments:\n
        i -- time in centiseconde
        
        Return a String"""
        
        cs = i % 100
        
        secondes = (i // 100) % 60
        
        minu = i // 6000
        
        if cs < 10:
            cs = "0" + str(cs)
        if secondes < 10:
            secondes = "0" + str(secondes)
        if minu < 10:
            minu = "0" + str(minu)
            
        return "{}:{}.{}".format(minu, secondes, cs)