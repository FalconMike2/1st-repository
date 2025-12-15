data=input("Kokia šiandienos data? ")
dien=data[8]+data[9]
men=data[5]+data[6]
met=data[0]+data[1]+data[2]+data[3]
newDay=int(dien)+1
newMet=met
newMen=men
if men== "04" or "06" or "09" or "11":
    if newDay>=31:
        newMen=int(men)+1
        dien="01"
    
    elif newDay<31:
        dien=newDay

    
if men== "01" or "03" or "05" or "07" or "08" or "10" or "12":
    if newDay>=32:
        newMen=int(men)+1
        dien="01"
    
    elif newDay<32:
        dien=newDay

if met==2008 or 2012 or 2016 or 2020 or 2024:
    if men=="02":
        if newDay>=30:
            dien="01"
            newMen=int(men)+1
    
        elif newDay<30:
            dien=newDay
            
if met == 2009 and 2010 and 2011 and 2013 and 2014 and 2015 and 2017 and 2018 and 2019 and 2021 and 2022 and 2023 and 2025:
    if men== "02":
        if newDay>=29:
            newMen=int(men)+1
            dien="01"
    
        elif newDay<29:
            dien=newDay            


if int(men)<=12 and newDay>=32:
    newMet=int(met)+1
    newMen="01"
    dien="01"
            
newData=str(newMet)+" "+str(newMen)+" "+str(dien)
print (newData)
