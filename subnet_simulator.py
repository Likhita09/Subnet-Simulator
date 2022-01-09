import ipaddress
from tkinter import *
root=Tk()
root.title("Subnet Simulator")  

def findClass(ip4):
    ip = int(ip4[0])
    if(ip >= 0 and ip <= 127):
        Label(frame3,font="arial 12", width=52, text="Class: A").pack()
        return "255.0.0.0"
   
    elif(ip >=128 and ip <= 191):
        Label(frame3,font="arial 12", width=52, text="Class: B").pack()
        return "255.255.0.0"
       
    elif(ip >= 192 and ip <= 223):
        Label(frame3,font="arial 12", width=52, text="Class: C").pack()
        return "255.255.255.0"
       
    elif(ip >= 224 and ip <= 239):
        return "D"
       
    else:
        return "E"

def net_mask(subnet):
    return format(int(subnet[0]),'08b')+'.'+format(int(subnet[1]),'08b')+'.'+format(int(subnet[2]),'08b')+'.'+format(int(subnet[3]),'08b')


def calculate():
    ip4 = ip.get().split(".")
    sub=findClass(ip4)
    def_bin = net_mask((sub.__str__()).split("."))
    ip_4 = ipaddress.ip_network(f'{ip.get()}/{bit.get()}', strict = False)
    net_bin=net_mask((ip_4.netmask.__str__()).split("."))
    host_bin = net_mask((ip_4.hostmask.__str__()).split("."))
    
    Label(frame3, font="arial 12", width=52,text="IP address: "+ip.get() ).pack()
    Label(frame3, font="arial 12", width=52,text="CIDR notation: "+ f'{ip.get()}/{bit.get()}' ).pack()
    Label(frame3, font="arial 12", width=52,text="Default subnet mask: "+sub ).pack()
    Label(frame3, font="arial 12", width=52,text="Default mask in Binary: "+def_bin ).pack()
    Label(frame3, font="arial 12", width=52, text="Subnet Mask: "+ip_4.netmask.__str__()).pack()
    Label(frame3, font="arial 12", width=52,text="Subnet Mask in Binary: "+net_bin ).pack()
    Label(frame3, font="arial 12", width=52,text="Wildcard mask: "+ip_4.hostmask.__str__() ).pack()
    Label(frame3, font="arial 12", width=52,text="Wildcard mask in Binary: "+host_bin ).pack()
    Label(frame3, font="arial 12", width=52, text="Network Address: "+ip_4.network_address.__str__()).pack()
    Label(frame3, font="arial 12", width=52, text="Broadcast Address: "+ip_4.broadcast_address.__str__()).pack()
    emptylabel = Label(frame3, font="arial 12", width=52, text="Usable Host IP range: "+(ip_4.network_address+1).__str__()+" - "+(ip_4.broadcast_address-1).__str__())
    emptylabel.pack()
    Label(frame3, font="arial 12", width=52, text="Total number of hosts: "+ip_4.num_addresses.__str__()).pack()
    Label(frame3, font="arial 12", width=52, text="Number of usable hosts: "+(ip_4.num_addresses-2).__str__()).pack()
    Label(frame4,font="arial 12").pack()


frame2 = Frame(root,padx=10, pady=10,relief=RIDGE)
frame2.grid(row=1, column=0)
frame3 = Frame(root,padx=10, pady=10, bd=5, relief=RIDGE)
frame3.grid(row=3, column=0)
frame4 = Frame(root)
frame4.grid(row=4, column=0)

label1=Label(frame2, text="Enter ip address:  ", font="arial 16")
label1.grid(row=0, column=0)

ip=Entry(frame2, font="arial 20 bold", width=20, borderwidth=10, bg="powder blue", justify="right")
ip.grid(row=0, column=1,columnspan=5, pady=10)

label2=Label(frame2, text="Enter subnet bits:  ", font="arial 16")
label2.grid(row=1, column=0)

bit=Entry(frame2, font="arial 20 bold", width=20, borderwidth=10, bg="powder blue", justify="right")
bit.grid(row=1, column=1,columnspan=5, pady=10)

btn = Button(frame2, command=calculate, text="Calculate", font="arial 16", bd=8,width=8)
btn.grid(row=4,column=1)

root.mainloop()
