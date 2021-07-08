import os

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from PIL import ImageTk, Image

# ======================================  Main Frame==================================

from fpdf import FPDF

# Import module
from tkinter import *

try:
    os.mkdir("Bill")
except:
    pass

splash_root = Tk()
spalsh_h = 480
spalsh_w = 600
splash_screen_w = splash_root.winfo_screenwidth()
splash_screen_h = splash_root.winfo_screenheight()
s_x = (splash_screen_w / 2) - (spalsh_w / 2)
s_y = (splash_screen_h / 2) - (spalsh_h / 2)
splash_root.geometry(f'{spalsh_w}x{spalsh_h}+{int(s_x)}+{int(s_y)}')
splash_root.title("Integer-i Billing Solutions")
# Set Label
canvas = Canvas(splash_root, width=600, height=480)
canvas.pack()
img = PhotoImage(file="integer.png")
canvas.create_image(300, 250, anchor=CENTER, image=img)


# main window function
def main():
    # destory splash window
    splash_root.destroy()

    # Execute tkinter
    root = Tk()

    # Adjust size

    root.title("Integer-i Billing Solutions")
    root_h = 730
    root_w = 1300
    root_screen_w = root.winfo_screenwidth()
    root_screen_h = root.winfo_screenheight()
    root_x = (root_screen_w / 2) - (root_w / 2)
    root_y = (root_screen_h / 2) - (root_h / 2)
    root.geometry(f'{root_w}x{root_h}+{int(root_x)}+{int(root_y)}')

    root.resizable(0, 0)
    root.config(bg="#DEEAEF")
    # ========================================Variables==============================

    product_name = StringVar()
    product_qty = StringVar()
    product_rate = StringVar()
    tex_enter = StringVar()
    customer_name = StringVar()
    customer_contact = StringVar()
    add_line1 = StringVar()
    add_line2 = StringVar()
    cus_gst_no = StringVar()
    date = StringVar()
    invoice_no = StringVar()
    state_code = StringVar()
    hsn_code = StringVar()
    frame_color = "#DEEAEF"

    # ================================== Function =================================

    Products_array = []

    def SubmitData():
        product_names = product_name.get()
        quantity = float(product_qty.get())
        rate = float(product_rate.get())
        hsn = hsn_code.get()
        total = float(quantity * rate)
        Products_array.append((product_names, hsn, quantity, rate, total))
        tree.delete(*tree.get_children())

        for data in (Products_array):
            tree.insert('', 'end', values=(data))
        product_name.set("")
        product_qty.set("")
        product_rate.set("")
        hsn_code.set("")
        pro_name_entry.focus_set()


    def getTotal():
        u = len(Products_array)
        total = 0
        for i in range(u):
            total = total + Products_array[i][4]
        getTotal.total = total

        total_label = Label(get_total_frame, text="Total:", font=("courier", 15))
        total_label.place(x=5, y=15)
        total_label_num = Label(get_total_frame, text=total, font=("courier", 15))
        total_label_num.place(x=75, y=15, width=250)

        # Tex
        tx = float(tex_enter.get()) / 100
        getTotal.total_tex = round(total * tx)
        tex_label = Label(get_total_frame, text="Total tex:", font=("courier", 15))
        tex_label.place(x=350, y=15)
        tex_label_num = Label(get_total_frame, text=getTotal.total_tex, font=("courier", 15))
        tex_label_num.place(x=480, y=15, width=250)

        getTotal.gross_total = round(getTotal.total_tex + total)
        gross_total_label = Label(get_total_frame, text="Grand total:", font=("courier", 15))
        gross_total_label.place(x=760, y=15)
        gross_total_label_num = Label(get_total_frame, text=getTotal.gross_total, font=("courier", 15))
        gross_total_label_num.place(x=885, y=15, width=250)

        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                 "Nineteen"]
        tens = [" ", " ", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        num = int(getTotal.gross_total)
        number_in_string11 = str(num)
        out = " "

        def converter(number, hundredvalue=0, thousandvalue=0, lakhvalue=0):
            if (number == 0):
                return " "

            elif (number > 0 and number <= 9):

                if (hundredvalue == 1):
                    return units[number] + " Hundred "

                elif (thousandvalue == 1):
                    return units[number] + " Thousand "

                elif (lakhvalue == 1):
                    return units[number] + " Lakh "

                else:
                    return (units[number])

            elif (number == 0 and hundredvalue == 1):
                return " "

            elif (number == 0 and thousandvalue == 1):
                return " "

            elif (number == 0 and lakhvalue == 1):
                return " "

            elif (number >= 10 and number <= 19):

                if (thousandvalue == 1):
                    return ((teens[(number % 10)]) + " Thousand ")

                elif (lakhvalue == 1):
                    return ((teens[(number % 10)]) + " Lakhs ")

                else:
                    return (teens[(number % 10)])

            elif (number >= 20 and number <= 99):

                number_in_string = str(number)
            if (thousandvalue == 1):
                return (tens[int(number_in_string[0])] + " " + units[int(number_in_string[1])] + " Thousand ")

            elif (lakhvalue == 1):
                return (tens[int(number_in_string[0])] + " " + units[int(number_in_string[1])] + " Lakhs ")

            else:
                return (tens[int(number_in_string[0])] + " " + units[int(number_in_string[1])])

        if (num > 0 and num <= 9):
            out = converter(num)

        elif (num >= 10 and num <= 19):
            out = converter(num)

        elif (num >= 20 and num <= 99):
            out = converter(num)

        elif (num >= 100 and num <= 999):
            out = converter(int(number_in_string11[0]), hundredvalue=1) + converter(int(number_in_string11[1::1]))

        elif (num >= 1000 and num <= 9999):
            out = converter(int(number_in_string11[0]), thousandvalue=1) + converter(int(number_in_string11[1]),
                                                                                     hundredvalue=1) + converter(
                int(number_in_string11[2::1]))

        elif (num >= 10000 and num <= 99999):
            out = converter(int(number_in_string11[0:2]), thousandvalue=1) + converter(int(number_in_string11[2]),
                                                                                       hundredvalue=1) + converter(
                int(number_in_string11[3::1]))

        elif (num >= 100000 and num <= 999999):
            out = converter(int(number_in_string11[0]), lakhvalue=1) + converter(int(number_in_string11[1:3]),
                                                                                 thousandvalue=1) + converter(
                int(number_in_string11[3]), hundredvalue=1) + converter(int(number_in_string11[4::1]))

        elif (num >= 1000000 and num <= 9999999):
            out = converter(int(number_in_string11[0:2]), lakhvalue=1) + converter(int(number_in_string11[2:4]),
                                                                                   thousandvalue=1) + converter(
                int(number_in_string11[4]), hundredvalue=1) + converter(int(number_in_string11[5:]))

        elif (num >= 10000000 and num <= 99999999):
            out = converter(int(number_in_string11[0])) + " Crore " + converter(int(number_in_string11[1:3]),
                                                                                lakhvalue=1) + converter(
                int(number_in_string11[3:5]), thousandvalue=1) + converter(int(number_in_string11[5]),
                                                                           hundredvalue=1) + converter(
                int(number_in_string11[6:]))

        elif (num >= 100000000 and num <= 999999999):
            out = converter(int(number_in_string11[0:2])) + " Crore " + converter(int(number_in_string11[2:4]),
                                                                                  lakhvalue=1) + converter(
                int(number_in_string11[4:6]), thousandvalue=1) + converter(int(number_in_string11[6]),
                                                                           hundredvalue=1) + converter(
                int(number_in_string11[7:]))

        elif (num >= 1000000000 and num <= 9999999999):
            out = converter(int(number_in_string11[0]), hundredvalue=1) + converter(
                int(number_in_string11[1:3])) + " Crore " + converter(int(number_in_string11[3:5]),
                                                                      lakhvalue=1) + converter(
                int(number_in_string11[5:7]),
                thousandvalue=1) + converter(
                int(number_in_string11[7]), hundredvalue=1) + converter(int(number_in_string11[8:]))
        getTotal.out1 = out + " Rupees"
        total_word_label = Label(get_total_frame, text="In Words :", font=("courier", 15))
        total_word_label.place(x=5, y=50)
        total_word_label_num = Label(get_total_frame, text=getTotal.out1, font=("courier", 15), justify="left")
        total_word_label_num.place(x=130, y=50, width=700)

    def delete_data():
        if not tree.selection():
            result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
        else:
            result = tkMessageBox.askquestion('', 'Are you sure you want to delete this item?', icon="warning")
            if result == 'yes':
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                tree.delete(curItem)
                print(tuple(selecteditem))
                print(type(selecteditem[4]))
                for item in range(len(Products_array)):
                    print(Products_array[item][4], float(selecteditem[4]))
                    if ((Products_array[item])[0] == selecteditem[0]):
                        if ((Products_array[item])[4] == float(selecteditem[4])):
                            break
                del (Products_array[item])
                print(Products_array)

    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', '', 8)
            self.cell(195, 5, '(Original / Duplicate)', border=0, align='R')
            self.ln(5)
            self.set_font('Arial', 'B', 15)
            self.cell(195, 8, 'TAX INVOICE', border=True, align='C')
            self.ln(10)

            self.set_font('Arial', '', 10)
            self.cell(85, 10, 'From,', align='L')
            self.cell(35, 10, 'Consignee,', align='R')
            self.ln(10)

            self.set_font('Arial', 'B', 10)
            self.cell(100, 5, 'Shree Raj Marble,', align='L', border=1)
            self.cell(95, 5, str(customer_name.get()), align='L', border=1)
            self.ln(5)

            self.set_font('Arial', '', 9)
            self.cell(100, 5, 'Address: Plot No. 16, Ranjeet sagar road,', align='L', border=1)
            self.cell(95, 5, "Address: " + str(add_line1.get()), align='L', border=1)
            self.ln(5)

            self.cell(100, 5, '                Jamnagar Gujarat, India.', align='L', border=1)
            self.cell(95, 5, "                " + str(add_line2.get()), align='L', border=1)
            self.ln(5)

            self.cell(100, 5, 'GST : 24ABBFS0185J1Z8', align='L', border=1)
            self.cell(95, 5, "Buyer's GST : " + str(cus_gst_no.get()), align='L', border=1)
            self.ln(5)
            self.ln(5)

            self.cell(65, 5, 'State Code : '+ str(state_code.get()), align='L', border=1)
            self.cell(65, 5, "Date: " + str(date.get()), align='L', border=1)
            self.cell(65, 5, "Invoice no. : " + str(invoice_no.get()), align='L', border=1)

            self.ln(10)

        # Page footer
        def footer(self):
            # Position at 1.5 cm from bottom
            self.set_y(-80)

            self.cell(140, 5, '', align='L', border=0)
            self.cell(55, 5, 'Total(Rs.)          : ' + str(getTotal.total), align='L', border=1)
            self.ln(5)

            self.cell(140, 5, '', align='L', border=0)
            self.cell(55, 5, "IGST"+ " ("+ str(float(tex_enter.get())/2)+"%)      :"+ str(float(getTotal.total_tex)/2), align='L', border=1)
            self.ln(5)

            self.cell(140, 5, '', align='L', border=0)
            self.cell(55, 5, "CGST"+" ("+str(float(tex_enter.get())/2)+"%)      :" + str(float(getTotal.total_tex)/2), align='L', border=1)
            self.ln(5)
            self.set_font('Arial', 'IB', 7)
            self.cell(140, 5, 'Grand Total(In words) : ' + str(getTotal.out1), align='L', border=1)
            self.set_font('Arial', '', 12)
            self.cell(55, 5, 'Grand Total(Rs.): ' + str(getTotal.gross_total), align='L', border=1)

            self.set_y(-60)
            # Arial italic 8
            self.set_font('Arial', 'I', 10)
            # Page number
            self.multi_cell(195, 4,
                            txt="Notes:-\n           1.We cannot accept responsibility for breakage,damage,theft or loss in transit \n             When the goods are handed over to the transport under clear receipt\n           2.In case of dispute, only Jamnagar Court will have jurdication.\n           3. The quality and quantity of the goods should be checked immediately of\n             receipt of material, otherwise no complaint will be entertained after one week \n \n                                                                                                                                                                 Shree Raj Marble\n  \n \n \n                                                                                                                                                            Authorised Signatory",
                            border=1, align="L")

            # self.multi_cell(70,5, txt="Shree Raj MArble\n \n \n \n Authorised Signatory",border=1,align="C")

        def bill_titles(self):
            # Arial 12
            self.line(10, 69.5, 10, 232)
            self.line(205, 69.5, 205, 232)
            self.line(10, 69.5, 205, 69.5)
            self.line(10, 232, 205, 232)
            self.line(30, 69.5, 30, 217)#sr
            self.line(80, 69.5, 80, 217)#product
            self.line(102, 69.5, 102, 217)#HSN
            self.line(132, 69.5, 132, 217)#Quen
            self.line(162, 69.5, 162, 217)#rate
            self.line(10,217,232,217)

            self.set_font('Arial', '', 12)
            # Background color
            self.set_fill_color(200, 220, 255)
            # Title
            self.cell(20, 6, 'Sr No', 0, 0, 'C', 1)
            self.cell(50, 6, 'Product Name', 0, 0, 'C', 1)
            self.cell(22, 6, 'HSN Code', 0, 0, 'C', 1)
            self.cell(30, 6, 'Quantity', 0, 0, 'C', 1)
            self.cell(30, 6, 'Rate', 0, 0, 'C', 1)
            self.cell(43, 6, 'Total', 0, 0, 'C', 1)
            # Line break
            self.ln(10)

        def add_products(self, list_products):
            i = 1
            for product in list_products:
                self.cell(20, 6, str(i), 0, 0, 'C')
                self.cell(50, 6, product[0], 0, 0, 'C')
                self.cell(22, 6, product[1], 0, 0, 'C')
                self.cell(30, 6, str(product[2]), 0, 0, 'C')
                self.cell(30, 6, str(product[3]), 0, 0, 'C')
                self.cell(43, 6, str(product[4]), 0, 0, 'C')
                self.ln(8)
                i += 1

    def printt(Products_array):
        MsgBox = tk.messagebox.askquestion('Print PDF?', 'Are you sure you want to Print the PDF', icon='question')
        if MsgBox == 'yes':
            pdf = PDF(format='A4', unit='mm')
            pdf.alias_nb_pages()
            pdf.add_page()
            pdf.set_font('Times', '', 12)
            pdf.bill_titles()
            pdf.add_products(Products_array)

            pdf.output(
                "Bill/" + str(
                    customer_name.get() + "_" + invoice_no.get()) + ".pdf")  # C:\Users\Public\Desktop\Bill             /Users/uttampagda/Desktop/Invoice/
        else:
            pass

    # =================================== Frames======================================
    shop_frame = Frame(root, bg=frame_color)
    shop_frame.place(x=0, y=0, height=25, width=1300)

    cus_detail_frame = Frame(root, bg=frame_color)
    cus_detail_frame.place(x=0, y=25, height=150, width=650)

    cus_exdetail_frame = Frame(root, bg=frame_color)
    cus_exdetail_frame.place(x=650, y=25, height=150, width=650)

    add_pro_frame = Frame(root, bg=frame_color)
    add_pro_frame.place(x=0, y=175, height=100, width=1300)

    show_items_frame = Frame(root, bg=frame_color)
    show_items_frame.place(x=0, y=275, height=250, width=1300)

    get_total_frame = Frame(root, bg=frame_color)
    get_total_frame.place(x=0, y=525, height=75, width=1300)

    print_frame = Frame(root, bg=frame_color)
    print_frame.place(x=0, y=650, height=80, width=1300)

    # ==================================== labels ==============================
    shop_name_lebel = Label(shop_frame, text="Shree Raj Marble", font=("arial", 23))
    shop_name_lebel.place(x=550, y=-5)

    cus_name_lebel = Label(cus_detail_frame, text="Customer name:", font=("courier", 17))
    cus_name_lebel.place(x=5, y=5)
    cus_name_entry = Entry(cus_detail_frame, textvariable=customer_name)
    cus_name_entry.place(x=250, y=7)

    add_lebel = Label(cus_detail_frame, text="Address line 1:", font=("courier", 17))
    add_lebel.place(x=5, y=35)
    add_entry = Entry(cus_detail_frame, textvariable=add_line1)
    add_entry.place(x=250, y=38)

    add1_lebel = Label(cus_detail_frame, text="Address line 2:", font=("courier", 17))
    add1_lebel.place(x=5, y=65)
    add1_entry = Entry(cus_detail_frame, textvariable=add_line2)
    add1_entry.place(x=250, y=68)

    cus_gst_lebel = Label(cus_detail_frame, text="Customer GST No:", font=("courier", 17))
    cus_gst_lebel.place(x=5, y=95)
    cus_gst_entry = Entry(cus_detail_frame, textvariable=cus_gst_no)
    cus_gst_entry.place(x=250, y=98)

    date_lebel = Label(cus_exdetail_frame, text="Date:", font=("courier", 17))
    date_lebel.place(x=5, y=5)
    date_entry = Entry(cus_exdetail_frame, textvariable=date)
    date_entry.place(x=250, y=8,width=130)

    invoice_no_lebel = Label(cus_exdetail_frame, text="Invoice no:", font=("courier", 17))
    invoice_no_lebel.place(x=5, y=35)
    invoice_no_entry = Entry(cus_exdetail_frame, textvariable=invoice_no)
    invoice_no_entry.place(x=250, y=38)

    state_code_lebel = Label(cus_exdetail_frame, text="State_code", font=("courier", 17))
    state_code_lebel.place(x=5, y=65)
    state_code_lebel_entry = Entry(cus_exdetail_frame, textvariable=state_code)
    state_code_lebel_entry.place(x=250, y=68)

    enter_tex_lebel = Label(cus_exdetail_frame, text="Tex (%):", font=("courier", 17))
    enter_tex_lebel.place(x=5, y=95)
    enter_tex_entry = Entry(cus_exdetail_frame, textvariable=tex_enter)
    enter_tex_entry.place(x=250, y=98)

    pro_name_lebel = Label(add_pro_frame, text="Product name:", font=("courier", 17))
    pro_name_lebel.place(x=5, y=5)
    pro_name_entry = Entry(add_pro_frame, textvariable=product_name)
    pro_name_entry.place(x=200, y=8, width=100)

    hsn_lebel = Label(add_pro_frame, text="HSN code:", font=("courier", 17))
    hsn_lebel.place(x=355, y=5)
    hsn_entry = Entry(add_pro_frame, textvariable=hsn_code)
    hsn_entry.place(x=500, y=8, width=80)

    qty_lebel = Label(add_pro_frame, text="Quentity:", font=("courier", 17))
    qty_lebel.place(x=650, y=5)
    qty_entry = Entry(add_pro_frame, textvariable=product_qty)
    qty_entry.place(x=790, y=8, width=100)

    rate_lebel = Label(add_pro_frame, text="Rate :", font=("courier", 17))
    rate_lebel.place(x=935, y=5)
    rate_entry = Entry(add_pro_frame, textvariable=product_rate)
    rate_entry.place(x=1035, y=8, width=100)

    add_pro_button = Button(add_pro_frame, text="ADD Product", command=SubmitData, padx=10, pady=10)
    add_pro_button.place(x=600, y=50)

    del_button = Button(show_items_frame, text="Delete", command=delete_data, padx=2, pady=1)
    del_button.place(x=1230, y=200)

    calculate_button = Button(get_total_frame, text="Calculate", command=getTotal)
    calculate_button.place(x=1230, y=5)

    print_bill_button = Button(print_frame, text="Print bill", command=lambda: printt(Products_array), padx=7, pady=5)
    print_bill_button.place(x=574, y=10)

    add_database_button = Button(print_frame, text="Add to Database", padx=7, pady=5)
    add_database_button.place(x=550, y=50)

    quit_button = Button(print_frame, text="Quit", command=root.destroy, padx=3, pady=2)
    quit_button.place(x=1260, y=50)

    rate_lebel = Label(print_frame, text="© Copyright Integer-i. All Rights Reserved", font=("courier", 13),
                       bg=frame_color)
    rate_lebel.place(x=10, y=125)



    style = ttk.Style()
    style.configure("Treeview", rowheight=30, background="silver", font=('Calibri', 20))
    scrollbarx = Scrollbar(show_items_frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(show_items_frame, orient=VERTICAL)
    tree = ttk.Treeview(show_items_frame, columns=("Product Name", "HSN code", "Quantity", "Rate", "Total"), height=240,
                        selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Product Name', text="Product Name", anchor=W)
    tree.heading('HSN code', text="HSN code", anchor=W)
    tree.heading('Quantity', text="Quantity", anchor=W)
    tree.heading('Rate', text="Rate", anchor=W)
    tree.heading('Total', text="Total", anchor=W)
    tree.column('#0', width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=300, anchor=tk.CENTER)
    tree.column('#2', stretch=NO, minwidth=0, width=200, anchor=tk.CENTER)
    tree.column('#3', stretch=NO, minwidth=0, width=200, anchor=tk.CENTER)
    tree.column('#4', stretch=NO, minwidth=0, width=200, anchor=tk.CENTER)
    tree.column('#5', stretch=NO, minwidth=0, width=200, anchor=tk.CENTER)
    tree.pack()


# Set Interval
splash_root.after(3000, main)

# Execute tkinter


# ========================================Backend================================


# =========================================== End===================================
mainloop()
