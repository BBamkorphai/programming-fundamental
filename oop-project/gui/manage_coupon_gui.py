import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import requests 
import json 

class ManageCoupon(tk.Frame): 
    def __init__(self,master): 
        super().__init__(master)
        self.event = None
        self.coupon_list = []
        self.get_couponwidget = [] 
        self.add_couponwidget = []
        self.modify_couponwidget = []
        self.create_widget()
        self.get_coupon_info()
        self.do_dropdown()

    def validate_num(self, char):
        if char.isdigit():
            return True
        else:
            return False

    def create_widget(self):  
        tk.Label(self,text="manage coupon", font=("Helvetica", 18)).place(x=290,y=30)
        
        self.back_to_admin_button = tk.Button(self,text="back",command=self.Back)
        self.back_to_admin_button.pack() 
        self.back_to_admin_button.place(x=800, y=5) 
        
    def get_coupon_info(self): 
        coupon_all = requests.get("http://127.0.0.1:8000/coupons/all").json()
        self.coupon_list = []
        for key in coupon_all: 
            components = [] 
            components.append(key)
            components.append(coupon_all[key]['name']) 
            components.append(coupon_all[key]['discount_value'])
            self.coupon_list.append(components) 

    def create_getcoupon_widget(self): 
        for item in self.get_couponwidget : 
            item.destroy()
        self.get_couponwidget = [] 
        for coupon in self.coupon_list: 
            self.button_widget = tk.Button(self,text=f"{coupon[0]} {coupon[1]} {coupon[2]}",command = lambda x=coupon[0],y=coupon[1],z=coupon[2]:self.modify_coupon(x,y,z))
            self.get_couponwidget.append(self.button_widget) 

    def add_coupon(self): 
        for item in self.add_couponwidget : 
            item.destroy()
        self.code_label = tk.Label(self, text="Code:") 
        self.code_label_input = tk.Entry(self)
        self.discount_label = tk.Label(self, text="Discount Value:")
        self.discount_label_input = tk.Entry(self, validate="key")
        self.discount_label_input['validatecommand'] = (self.discount_label_input.register(self.validate_num), '%S') 
        self.name_label = tk.Label(self, text="Name:")
        self.name_label_input = tk.Entry(self)   
        self.title = tk.Label(self, text="Add coupon")
        self.summit_button_label = tk.Button(self,text="summit",command=self.submit_button)
        self.add_couponwidget = [self.code_label,self.code_label_input,self.discount_label,self.discount_label_input,self.name_label,self.name_label_input,self.title,self.summit_button_label]

    def show_add_coupon(self): 
        for i,widget in enumerate(self.add_couponwidget): 
            widget.pack(in_ = self) 
            widget.place(x=300,y=100+ 30*i)

    def hide_add_coupon(self): 
        for widget in self.add_couponwidget:  
            widget.pack(in_ = None) 
            widget.pack_forget()
    
    def modify_coupon(self,code,name,discount_value): 
        self.hide_getwidget() 
        self.create_modify_widget(code,name,discount_value) 
        self.show_modify() 

    def update_coupon(self,code): 
        name = self.mname_label_input.get() 
        discount_value = self.mdiscount_label_input.get()  
        if not discount_value.isdigit(): 
            messagebox.showinfo(title="notification",message="discount_value must be integer")
            return
        
        if float(discount_value) <= 0 or float(discount_value) > 100: 
            messagebox.showinfo(title="notification",message="discount_value must be positive integer") 
            return
        dict_put = {code:{"name":name,"discount_value":discount_value}}
        message = requests.put("http://127.0.0.1:8000/coupons/all",data=json.dumps(dict_put))

        self.mname_label_input.delete(0,tk.END)
        self.mdiscount_label_input.delete(0,tk.END) 
        self.get_coupon_info()
        self.handle_selection(self.event)

    def delete_button(self,code):  
        dict_delete = {"code":code}
        message = requests.delete("http://127.0.0.1:8000/coupons/all",data=json.dumps(dict_delete))
        self.get_coupon_info()
        self.handle_selection(self.event)

    def submit_button(self):  
        name = self.name_label_input.get() 
        code = self.code_label_input.get() 
        discount_value = self.discount_label_input.get()  
        if not discount_value.isdigit(): 
            messagebox.showinfo(title="notification",message="discount_value must be integer")
            return 
        if float(discount_value) <= 0 or float(discount_value) > 100: 
            messagebox.showinfo(title="notification",message="discount_value must be 0 - 100") 
            return
        dict_add = {code:{"name":name, "discount_value":discount_value}}
        for coupon in self.coupon_list:  
            if coupon[0] == code : 
                messagebox.showinfo(title="notification",message="this code had already added")
                return
        message = requests.post("http://127.0.0.1:8000/coupons/all",data=json.dumps(dict_add))
        self.name_label_input.delete(0,tk.END) 
        self.code_label_input.delete(0,tk.END) 
        self.discount_label_input.delete(0,tk.END)
        self.get_coupon_info()   
    
    def create_modify_widget(self,code,name,discount_value): 
        for item in self.modify_couponwidget : 
            item.destroy()
        self.mdiscount_label = tk.Label(self, text="Discount Value:")
        self.mdiscount_label_input = tk.Entry(self, validate="key")
        self.mdiscount_label_input['validatecommand'] = (self.mdiscount_label_input.register(self.validate_num), '%S')  
        self.mdiscount_label_input.insert(0,discount_value)
        self.mname_label = tk.Label(self, text="Name:")
        self.mname_label_input = tk.Entry(self)  
        self.mname_label_input.insert(0,name)
        self.mtitle = tk.Label(self, text="mofidy")
        self.modify_button_label = tk.Button(self,text="update",command= lambda x=code : self.update_coupon(x))
        self.delete_button_label = tk.Button(self,text="delete",command= lambda x=code : self.delete_button(x))
        self.modify_couponwidget = [self.mdiscount_label,self.mdiscount_label_input,self.mname_label,self.mname_label_input,self.mtitle,self.modify_button_label,self.delete_button_label]

    def hide_modify(self): 
        for m_widget in self.modify_couponwidget: 
            m_widget.pack(in_ =None) 
            m_widget.pack_forget()

    def show_modify(self): 
        for i,m_widget in enumerate(self.modify_couponwidget): 
            m_widget.pack(in_ =self) 
            m_widget.place(x=300,y=100 + 50*i)

    def do_dropdown(self): 
        self.choice = tk.StringVar(self, value="chose to do")
        self.combo = ttk.Combobox(self, textvariable=self.choice)
        self.combo["values"] = ("add coupon","modify coupon")
        self.combo.bind("<<ComboboxSelected>>",self.handle_selection)
        self.combo.place(x = 550, y = 50) 
    
    def handle_selection(self,event):
        self.event = event
        print(self.choice.get())
        if self.choice.get() == "modify coupon": 
            self.hide_add_coupon()
            self.hide_modify()
            self.create_getcoupon_widget()
            self.show_getwidget()
        
        elif self.choice.get() == "add coupon":
            self.hide_getwidget() 
            self.hide_modify()
            self.add_coupon() 
            self.show_add_coupon()

    def show_getwidget(self): 
        for i,coupon in enumerate(self.get_couponwidget):
            coupon.pack(in_ = self)
            coupon.place(x = 300,y = 100 + 50*i)
    
    def hide_getwidget(self): 
        for coupon in self.get_couponwidget: 
            coupon.pack(in_ = None)
            coupon.pack_forget()

    def Back(self): 
        self.master.show_admin()