import tkinter as tk
import time
import json
import requests
from threading import Thread
import hashlib
import hmac

# Config
if 1==1:

    start_asset1 = "ETH"
    start_asset2 = "USDT"
    
    # Color
    c_red = "#ffc0cb"
    c_green = "#d9ffd9"

# Tkinter start
root = tk.Tk()
root.title ("ETG v1.0 for Binance")
root.geometry ("1110x615+350+100")
root.resizable(0, 0)

# Main Assets
if 1==1:
    
    coord_x = 450
    coord_y = 20

    # Background
    bg_main_asset = tk.Label (root, relief="ridge", bg="#559900")
    bg_main_asset.place (x=coord_x, y=coord_y, width=200, height=65)

    def asset_load():

        try:
            save_file = open ("etg_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)
            
        except Exception as e:
            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <LOAD FILE FAIL>\nEXCEPTION: " + str(e) + "\n\n")
            return


        if l_next.cget ("text") == "0":
            
            l_next.configure (text="1")

            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("1.0", "1.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("2.0", "2.end"))

        elif l_next.cget ("text") == "1":
            
            l_next.configure (text="2")

            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("3.0", "3.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("4.0", "4.end"))

        elif l_next.cget ("text") == "2":
            
            l_next.configure (text="3") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("5.0", "5.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("6.0", "6.end"))
        
        elif l_next.cget ("text") == "3":
            
            l_next.configure (text="4") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("7.0", "7.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("8.0", "8.end"))
        
        elif l_next.cget ("text") == "4":
            
            l_next.configure (text="5") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("9.0", "9.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("10.0", "10.end"))
        
        elif l_next.cget ("text") == "5":
            
            l_next.configure (text="1") 
        
            e_main_asset1.delete (0, "end")
            e_main_asset1.insert (0, t_save.get ("1.0", "1.end"))
            e_main_asset2.delete (0, "end")
            e_main_asset2.insert (0, t_save.get ("2.0", "2.end"))

    def asset_save():
        
        try:
            save_file = open ("etg_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)
        
        except:
            t_save.delete ("1.0", "end")
            
            for i in range (1, 13):
                t_save.insert ( str(i) + ".0", "\n")

        if l_next.cget ("text") == "0":
            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <STATE 0 SAVE NOT POSSIBLE>\n\n")
        elif l_next.cget ("text") == "1":
            t_save.delete ("1.0", "3.0")
            t_save.insert ("1.0", e_main_asset1.get() + "\n")
            t_save.insert ("2.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "2":
            t_save.delete ("3.0", "5.0")
            t_save.insert ("3.0", e_main_asset1.get() + "\n")
            t_save.insert ("4.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "3":
            t_save.delete ("5.0", "7.0")
            t_save.insert ("5.0", e_main_asset1.get() + "\n")
            t_save.insert ("6.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "4":
            t_save.delete ("7.0", "9.0")
            t_save.insert ("7.0", e_main_asset1.get() + "\n")
            t_save.insert ("8.0", e_main_asset2.get() + "\n")
        elif l_next.cget ("text") == "5":
            t_save.delete ("9.0", "11.0")
            t_save.insert ("9.0", e_main_asset1.get() + "\n")
            t_save.insert ("10.0", e_main_asset2.get() + "\n")

        # Save
        new_save = open ("etg_binance.txt" , "w")
        new_save.write (t_save.get("1.0", "13.0"))
        new_save.close()

    e_main_asset1 = tk.Entry(root, font=('Courier New', 14, 'bold'))
    e_main_asset1.place (x=coord_x + 25, y=coord_y + 35, width=75, height=20)
    e_main_asset1.insert (0, start_asset1)

    e_main_asset2 = tk.Entry(root, font=('Courier New', 14, 'bold'))
    e_main_asset2.place (x=coord_x + 110, y=coord_y + 35, width=75, height=20)
    e_main_asset2.insert (0, start_asset2)

    b_main_asset_load = tk.Button (root, font=('Courier New', 10, 'bold'), text="NEXT", command=asset_load)
    b_main_asset_load.place (x=coord_x + 25, y=coord_y + 10, width=60, height=20)

    b_main_asset_save = tk.Button (root, font=('Courier New', 10, 'bold'), text="SAVE", command=asset_save)
    b_main_asset_save.place (x=coord_x + 125, y=coord_y + 10, width=60, height=20)

    l_next = tk.Label(root, text="0", font=('Courier New', 16, 'bold'),relief="ridge", bg="#66CCFF")
    l_next.place (x=coord_x + 92, y=coord_y + 5, width=26, height=26)

    l_credit = tk.Label(root, text="Github: Frosti2020", font=('Courier New', 10, 'bold'))
    l_credit.place (x=coord_x + 210, y=coord_y + 50, height=18)



# Price
if 1==1:

    coord_x = 10
    coord_y = 90
    
    # Background
    bg_price = tk.Label (root,relief="ridge", bg="#FFCC99")
    bg_price.place (x=coord_x, y=coord_y, width=230, height=85)

    class thread_get_price(Thread):
        def run(self):

            url_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            
            try:
                r = requests.get(url=url_price, timeout=4)

                the_price = r.json() ["price"]
                
                # Cut Zero and point at end of price
                while the_price[-1] == "0":
                    the_price = the_price[:-1]
                if the_price[-1] == ".":
                    the_price = the_price[:-1]

                e_price.delete (0, "end")
                e_price.insert (0, the_price)
                l_price_time.configure (text=time.strftime("%d.%m.%y %H:%M:%S"))

                # Confirmation
                bg_price.configure (bg="green")
                time.sleep (0.2)
                bg_price.configure (bg="#FFCC99")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET PRICE FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def get_price():
        tgp = thread_get_price()
        tgp.start()
        
    def set_price_buy():
        e_trade_price_buy.delete(0, "end")
        e_trade_price_buy.insert (0, e_price.get())
    def set_price_sell():
        e_trade_price_sell.delete(0, "end")
        e_trade_price_sell.insert (0, e_price.get())

    b_price = tk.Button(root, text="Price", command=get_price)
    b_price.place(x=coord_x + 10, y=coord_y + 10, width=50, height=50)

    e_price = tk.Entry(root, font=('Courier New', 14, 'bold'))
    e_price.place(x=coord_x + 70, y=coord_y + 10, width=150, height=25)

    b_price_buy = tk.Button(root, text="BUY", command=set_price_buy)
    b_price_buy.place(x=coord_x + 70, y=coord_y + 40, width=70, height=20)

    b_price_sell = tk.Button(root, text="SELL", command=set_price_sell)
    b_price_sell.place(x=coord_x + 150, y=coord_y + 40, width=70, height=20)

    l_price_time = tk.Label(root, text="00.00.00 00:00:00", font=('Courier New', 12, 'bold'), bg="#FFCC99", fg="#6f00ff")
    l_price_time.place (x=coord_x + 10, y=coord_y + 63, height=18)

# Asset1 Funds
if 1==1:

    coord_x = 250
    coord_y = 90
    
    # Background
    bg_asset1 = tk.Label (root,relief="ridge", bg="#99CC99")
    bg_asset1.place (x=coord_x, y=coord_y, width=300, height=85)
    
    def all_funds():
        global check_funds
        check_funds = 1

        ts = thread_assets()
        ts.start()
    
    class thread_assets(Thread):
        def run(self):

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()

            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/account?"
            query = "timestamp=" + t_str

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.get (url_rdy, headers=header)

                balance_list = r.json() ["balances"]

                for i in range (0, len(balance_list)):
                    
                    if balance_list[i] ["asset"] == e_main_asset1.get().upper():
                        
                        # Cut Zero and point at end of funds
                        if float(balance_list[i]["free"]) >= 1:
                            free = str(float(balance_list[i]["free"]))
                        elif float(balance_list[i]["free"]) == 0:
                            free = "0.0"
                        else:
                            free = "%.8f" % float(balance_list[i]["free"])
                            
                            while free[-1] == "0":
                                free = free[:-1]

                        if float(balance_list[i]["locked"]) >= 1:
                            locked = str(float(balance_list[i]["locked"]))
                        elif float(balance_list[i]["locked"]) == 0:
                            locked = "0.0"
                        else:
                            locked = "%.8f" % float(balance_list[i]["locked"])
                            
                            while locked[-1] == "0":
                                locked = locked[:-1]

                        l_funds_asset1.configure (text=balance_list[i]["asset"])
                        e_funds_asset1_free.delete(0, "end")
                        e_funds_asset1_free.insert(0, free)
                        e_funds_asset1_locked.delete(0, "end")
                        e_funds_asset1_locked.insert(0, locked)

                    if balance_list[i] ["asset"] == e_main_asset2.get().upper():

                        # Cut Zero and point at end of funds
                        if float(balance_list[i]["free"]) >= 1:
                            free = str(float(balance_list[i]["free"]))
                        elif float(balance_list[i]["free"]) == 0:
                            free = "0.0"
                        else:
                            free = "%.8f" % float(balance_list[i]["free"])
                            
                            while free[-1] == "0":
                                free = free[:-1]

                        if float(balance_list[i]["locked"]) >= 1:
                            locked = str(float(balance_list[i]["locked"]))
                        elif float(balance_list[i]["locked"]) == 0:
                            locked = "0.0"
                        else:
                            locked = "%.8f" % float(balance_list[i]["locked"])
                            
                            while locked[-1] == "0":
                                locked = locked[:-1]

                        l_funds_asset2.configure (text=balance_list[i]["asset"])
                        e_funds_asset2_free.delete(0, "end")
                        e_funds_asset2_free.insert(0, free)
                        e_funds_asset2_locked.delete(0, "end")
                        e_funds_asset2_locked.insert(0, locked)

                    # Check All Funds
                    global check_funds
                    if check_funds == 1:

                        if float(balance_list[i] ["free"]) > 0 or float(balance_list[i] ["locked"]) > 0:

                            # Cut Zero and point at end of funds
                            if float(balance_list[i]["free"]) >= 1:
                                free = str(float(balance_list[i]["free"]))
                            elif float(balance_list[i]["free"]) == 0:
                                free = "0.0"
                            else:
                                free = "%.8f" % float(balance_list[i]["free"])
                                
                                while free[-1] == "0":
                                    free = free[:-1]

                            if float(balance_list[i]["locked"]) >= 1:
                                locked = str(float(balance_list[i]["locked"]))
                            elif float(balance_list[i]["locked"]) == 0:
                                locked = "0.0"
                            else:
                                locked = "%.8f" % float(balance_list[i]["locked"])
                                
                                while locked[-1] == "0":
                                    locked = locked[:-1]

                            t_log.insert ("1.0", balance_list[i]["asset"] + "\n"
                                                + free + "\n"
                                                + locked + "\n\n", "bg_funds")

                if check_funds == 1:
                    t_log.insert ("1.0", "ALL FUNDS:\n")
                    t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")

                check_funds = 0

                # Confirmation
                bg_asset1.configure (bg="green")
                bg_asset2.configure (bg="green")
                time.sleep (0.2)
                bg_asset1.configure (bg="#99CC99")
                bg_asset2.configure (bg="#99CC99")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET FUNDS FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def amount_assets():
        global check_funds
        check_funds = 0
        
        ts = thread_assets()
        ts.start()
    
    b_funds_asset1 = tk.Button(root, text="Funds", command=amount_assets)
    b_funds_asset1.place(x=coord_x + 10, y=coord_y + 10, width=60, height=20)

    b_funds_allfunds = tk.Button(root, text="All Funds", command=all_funds)
    b_funds_allfunds.place(x=coord_x + 210, y=coord_y + 10, width=80, height=20)

    l_funds_asset1_free = tk.Label(root, text="Free", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset1_free.place (x=coord_x + 10, y=coord_y + 35, height=20)

    l_funds_asset1_locked = tk.Label(root, text="Locked", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset1_locked.place (x=coord_x + 10, y=coord_y + 55, height=20)

    l_funds_asset1 = tk.Label(root, text="ETH", font=('Courier New', 14, 'bold'), bg="#99CC99")
    l_funds_asset1.place(x=coord_x + 90, y=coord_y + 10, height=20)

    e_funds_asset1_free = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset1_free.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_funds_asset1_locked = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset1_locked.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

# Asset2 Funds
if 1==1:

    coord_x = 560
    coord_y = 90
    
    # Background
    bg_asset2 = tk.Label (root,relief="ridge", bg="#99CC99")
    bg_asset2.place (x=coord_x, y=coord_y, width=300, height=85)
    
    b_funds_asset2 = tk.Button(root, text="Funds", command=amount_assets)
    b_funds_asset2.place(x=coord_x + 10, y=coord_y + 10, width=60, height=20)

    l_funds_asset2_free = tk.Label(root, text="Free", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset2_free.place (x=coord_x + 10, y=coord_y + 35, height=20)

    l_funds_asset2_locked = tk.Label(root, text="Locked", font=('Courier New', 10, 'bold'), bg="#99CC99")
    l_funds_asset2_locked.place (x=coord_x + 10, y=coord_y + 55, height=20)

    l_funds_asset2 = tk.Label(root, text="USDT", font=('Courier New', 14, 'bold'), bg="#99CC99")
    l_funds_asset2.place(x=coord_x + 90, y=coord_y + 10, height=20)

    e_funds_asset2_free = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset2_free.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_funds_asset2_locked = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_funds_asset2_locked.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

# Calculator 1
if 1==1:

    coord_x = 10
    coord_y = 185
    
    # Background
    bg_cal1 = tk.Label (root,relief="ridge", bg="#A9E2F3")
    bg_cal1.place (x=coord_x, y=coord_y, width=230, height=80)

    def cal1_price():
        e_cal1_value1.delete (0, "end")
        e_cal1_value1.insert (0, e_price.get())
    def cal1_cal():

        if e_cal1_value1.get() == "" or e_cal1_value2.get() == "":
            return

        cal1_result = "%.10f" % (float(e_cal1_value2.get()) * float(e_cal1_value1.get()))

        # Max lenght 12 Char
        while len(cal1_result) > 12:
            cal1_result = cal1_result[:-1]

        # Cut Zero and point at end of price
        while cal1_result[-1] == "0" and cal1_result.find(".") > -1:
            
            cal1_result = cal1_result[:-1]

        if cal1_result[-1] == ".":
            cal1_result = cal1_result[:-1]

        e_cal1_result.delete (0, "end")
        e_cal1_result.insert (0, cal1_result)

    b_cal1_price = tk.Button(root, text="Price", command=cal1_price)
    b_cal1_price.place(x=coord_x + 10, y=coord_y + 10, width=50, height=20)

    b_cal1_cal = tk.Button(root, text="Cal", command=cal1_cal)
    b_cal1_cal.place(x=coord_x + 10, y=coord_y + 35, width=50, height=35)

    e_cal1_value1 = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_cal1_value1.place(x=coord_x + 70, y=coord_y + 10, width=150, height=18)

    e_cal1_value2 = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_cal1_value2.place(x=coord_x + 70, y=coord_y + 30, width=150, height=18)
    
    e_cal1_result = tk.Entry(root, font=('Courier New', 12, 'bold'))
    e_cal1_result.place(x=coord_x + 70, y=coord_y + 50, width=150, height=20)

# Calculator 2
if 1==1:

    coord_x = 10
    coord_y = 275

    # Background
    bg_cal2 = tk.Label (root,relief="ridge", bg="#A9E2F3")
    bg_cal2.place (x=coord_x, y=coord_y, width=230, height=80)

    def cal2_price():
        e_cal2_value1.delete (0, "end")
        e_cal2_value1.insert (0, e_price.get())

    def cal2_diff():

        if e_cal2_value1.get() == "" or e_cal2_value2.get() == "":
            return

        cal2_result = "%.2f" % (float(e_cal2_value2.get()) / (float(e_cal2_value1.get()) / 100) - 100)
        
        # Cut Zero and point at end of price
        while cal2_result[-1] == "0" and cal2_result.find(".") > -1:
            cal2_result = cal2_result[:-1]

            if cal2_result[-1] == ".":
                cal2_result = cal2_result[:-1]

        # Color the result
        if cal2_result.find('-') == -1:
            
            cal2_result = ("+" + cal2_result + " %")
            l_cal2_result.configure (fg="green")
        
        else:
            
            cal2_result = (cal2_result + " %")
            l_cal2_result.configure (fg="#CD0000")

        # really?
        if len(cal2_result) > 11:
            cal2_result = "really?"

        l_cal2_result.configure (text=cal2_result)

    b_cal1_price = tk.Button(root, text="Price", command=cal2_price)
    b_cal1_price.place(x=coord_x + 10, y=coord_y + 10, width=50, height=20)
    
    b_cal2_cal = tk.Button(root, text="Diff", command=cal2_diff)
    b_cal2_cal.place(x=coord_x + 10, y=coord_y + 35, width=50, height=35)

    e_cal2_value1 = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_cal2_value1.place(x=coord_x + 70, y=coord_y + 10, width=150, height=18)

    e_cal2_value2 = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_cal2_value2.place(x=coord_x + 70, y=coord_y + 30, width=150, height=18)
    
    l_cal2_result = tk.Label(root, text="000.00%", font=('Courier New', 14, 'bold'), bg="#A9E2F3")
    l_cal2_result.place(x=coord_x + 70, y=coord_y + 52, width=150, height=20)

# Calculator 3
if 1==1:

    coord_x = 10
    coord_y = 365
    
    # Background
    bg_cal3 = tk.Label (root,relief="ridge", bg="#A9E2F3")
    bg_cal3.place (x=coord_x, y=coord_y, width=230, height=80)

    def cal3_price():
        e_cal3_value1.delete (0, "end")
        e_cal3_value1.insert (0, e_price.get())

    def cal3_cal():

        if e_cal3_value1.get() == "" or e_cal3_value2.get() == "":
            return

        cal3_result = "%.10f" % (float(e_cal3_value1.get()) / 100 * float(e_cal3_value2.get()) + float(e_cal3_value1.get()))

        # Max lenght 12 Char
        while len(cal3_result) > 12:
            cal3_result = cal3_result[:-1]

        # Cut Zero and point at end of price
        while cal3_result[-1] == "0" and cal3_result.find(".") > -1:
            
            cal3_result = cal3_result[:-1]

        if cal3_result[-1] == ".":
            cal3_result = cal3_result[:-1]

        e_cal3_result.delete (0, "end")
        e_cal3_result.insert (0, cal3_result)

    b_cal3_price = tk.Button(root, text="Price", command=cal3_price)
    b_cal3_price.place(x=coord_x + 10, y=coord_y + 10, width=50, height=20)

    b_cal3_cal = tk.Button(root, text="Cal", command=cal3_cal)
    b_cal3_cal.place(x=coord_x + 10, y=coord_y + 35, width=50, height=35)

    e_cal3_value1 = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_cal3_value1.place(x=coord_x + 70, y=coord_y + 10, width=150, height=18)

    e_cal3_value2 = tk.Entry(root, font=('Courier New', 10, 'bold'))
    e_cal3_value2.place(x=coord_x + 70, y=coord_y + 30, width=100, height=18)

    l_cal3_pro = tk.Label(root, text="%", font=('Courier New', 14, 'bold'), bg="#A9E2F3")
    l_cal3_pro.place(x=coord_x + 170, y=coord_y + 30, height=20)
    
    e_cal3_result = tk.Entry(root, font=('Courier New', 12, 'bold'))
    e_cal3_result.place(x=coord_x + 70, y=coord_y + 50, width=150, height=20)

# Trade buy
if 1==1:

    coord_x = 250
    coord_y = 185

    # Background
    bg_trade_buy = tk.Label (root,relief="ridge", bg=c_green)
    bg_trade_buy.place (x=coord_x, y=coord_y, width=300, height=105)

    def order_buy():

        if e_trade_price_buy.get() == "" or e_trade_amount_buy.get() == "":
            return
        
        global the_side, the_price, the_amount
        the_side = "BUY"
        the_price = e_trade_price_buy.get()
        the_amount = e_trade_amount_buy.get()

        tt = thread_trades()
        tt.start()

    b_trade_buy = tk.Button(root, text="BUY", command=order_buy)
    b_trade_buy.place(x=coord_x + 90 , y=coord_y + 10, width=200, height=20)

    l_trade_price_buy = tk.Label(root, text="Price", font=('Courier New', 10, 'bold'), bg=c_green)
    l_trade_price_buy.place (x=coord_x + 10, y=coord_y + 35, height=18)
    
    l_trade_amount_buy = tk.Label(root, text="Amount", font=('Courier New', 10, 'bold'), bg=c_green)
    l_trade_amount_buy.place (x=coord_x + 10, y=coord_y + 55, height=18)

    l_trade_id_buy = tk.Label(root, text="ID", font=('Courier New', 10, 'bold'), bg=c_green)
    l_trade_id_buy.place (x=coord_x + 10, y=coord_y + 75, height=18)

    e_trade_price_buy = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_price_buy.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_trade_amount_buy = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_amount_buy.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

    e_trade_id_buy = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_id_buy.place (x=coord_x + 90, y=coord_y + 75, width=200, height=18)

# Trade sell
if 1==1:

    coord_x = 560
    coord_y = 185

    # Background
    bg_trade_sell = tk.Label (root,relief="ridge", bg=c_red)
    bg_trade_sell.place (x=coord_x, y=coord_y, width=300, height=105)

    def order_sell():

        if e_trade_price_sell.get() == "" or e_trade_amount_sell.get() == "":
            return
        
        global the_side, the_price, the_amount
        the_side = "SELL"
        the_price = e_trade_price_sell.get()
        the_amount = e_trade_amount_sell.get()

        tt = thread_trades()
        tt.start()

    class thread_trades(Thread):
        def run(self):

            global the_side, the_price, the_amount
           
            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()

            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/order?"

            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            side = "&side=" + the_side
            the_type = "&type=LIMIT"
            timeinforce = "&timeInForce=GTC"
            amount = "&quantity=" + the_amount
            price = "&price=" + the_price
            zeit = "&timestamp=" + t_str
            query = symbol + side + the_type + timeinforce + amount + price + zeit

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.post (url_rdy, headers=header, timeout=4)

                # BG for order
                if r.json() ["side"] == "BUY":
                    bg_use = "bg_green"
                else:
                    bg_use = "bg_red"

                t_log.insert ("1.0",   "ORDER " + the_side + ":\n"
                                        + "ID    : " + str(r.json() ["orderId"]) + "\n"
                                        + "PRICE : "  + str(float(r.json() ["price"])) + "\n"
                                        + "AMOUNT: " + str(float(r.json() ["origQty"])) + "\n"
                                        + "FILLED: " + str(float(r.json() ["executedQty"])) + "\n\n", bg_use)

                t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")

                if the_side == "BUY":
                    e_trade_price_buy.delete (0, "end")
                    e_trade_amount_buy.delete (0, "end")
                    e_trade_id_buy.delete (0, "end")
                    e_trade_id_buy.insert (0, r.json() ["orderId"])
                else:
                    e_trade_price_sell.delete (0, "end")
                    e_trade_amount_sell.delete (0, "end")
                    e_trade_id_sell.delete (0, "end")
                    e_trade_id_sell.insert (0, r.json() ["orderId"])

                # Confirmation
                if the_side == "BUY":
                    bg_trade_buy.configure (bg="green")
                    time.sleep (0.2)
                    bg_trade_buy.configure (bg=c_green)
                else:
                    bg_trade_sell.configure (bg="green")
                    time.sleep (0.2)
                    bg_trade_sell.configure (bg=c_red)
            
            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <ORDER " + the_side + " FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")
    
    b_trade_sell = tk.Button(root, text="SELL", command=order_sell)
    b_trade_sell.place(x=coord_x + 90 , y=coord_y + 10, width=200, height=20)

    l_trade_price_sell = tk.Label(root, text="Price", font=('Courier New', 10, 'bold'), bg=c_red)
    l_trade_price_sell.place (x=coord_x + 10, y=coord_y + 35, height=18)
    
    l_trade_amount_sell = tk.Label(root, text="Amount", font=('Courier New', 10, 'bold'), bg=c_red)
    l_trade_amount_sell.place (x=coord_x + 10, y=coord_y + 55, height=18)

    l_trade_id_sell = tk.Label(root, text="ID", font=('Courier New', 10, 'bold'), bg=c_red)
    l_trade_id_sell.place (x=coord_x + 10, y=coord_y + 75, height=18)

    e_trade_price_sell = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_price_sell.place (x=coord_x + 90, y=coord_y + 35, width=200, height=18)

    e_trade_amount_sell = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_amount_sell.place (x=coord_x + 90, y=coord_y + 55, width=200, height=18)

    e_trade_id_sell = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_trade_id_sell.place (x=coord_x + 90, y=coord_y + 75, width=200, height=18)

# Order ID Info
if 1==1:

    coord_x = 250
    coord_y = 300

    # Background
    bg_idinfo = tk.Label (root,relief="ridge", bg="#F5DA81")
    bg_idinfo.place (x=coord_x, y=coord_y, width=300, height=145)

    class thread_id_info(Thread):
        def run(self):

            if e_idinfo.get() == "":
                return

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()

            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/order?"

            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            orderid = "&orderId=" + e_idinfo.get()
            q_time = "&timestamp=" + t_str
            query = symbol + orderid + q_time

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.get (url_rdy, headers=header, timeout=4)
                
                l_idinfo_side.configure (text=r.json() ["side"])
                l_idinfo_price.configure (text=str(float(r.json() ["price"])))
                l_idinfo_amount.configure (text=str(float(r.json() ["origQty"])))
                l_idinfo_filled.configure (text=str(float(r.json() ["executedQty"])))
                l_idinfo_status.configure (text=r.json() ["status"])
                
                # Confirmation
                bg_idinfo.configure (bg="green")
                time.sleep (0.2)
                bg_idinfo.configure (bg="#F5DA81")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET ID-INFO FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def id_info():
        tii = thread_id_info()
        tii.start()

    def id_info_add():

        e_idinfo.delete (0, "end")
        try:
            e_idinfo.insert (0, e_trade_id_buy.selection_get())
        except:
            try:
                e_idinfo.insert (0, e_trade_id_sell.selection_get())
            except:
                try:
                    e_idinfo.insert (0, t_log.selection_get())
                except:
                    pass

    b_idinfo = tk.Button(root, text="ID-Info", command=id_info)
    b_idinfo.place(x=coord_x + 10 , y=coord_y + 10, width=60, height=18)

    b_idinfo_buy = tk.Button(root, text="ADD", command=id_info_add)
    b_idinfo_buy.place(x=coord_x + 90 , y=coord_y + 10, width=40, height=18)

    e_idinfo = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_idinfo.place (x=coord_x + 135, y=coord_y + 10, width=155, height=18)

    l_idinfo_name_side = tk.Label(root, text="Side", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_side.place (x=coord_x + 10, y=coord_y + 35, height=18)

    l_idinfo_name_price = tk.Label(root, text="Price", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_price.place (x=coord_x + 10, y=coord_y + 55, height=18)
    
    l_idinfo_name_amount = tk.Label(root, text="Amount", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_amount.place (x=coord_x + 10, y=coord_y + 75, height=18)

    l_idinfo_name_filled = tk.Label(root, text="Filled", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_filled.place (x=coord_x + 10, y=coord_y + 95, height=18)

    l_idinfo_name_status = tk.Label(root, text="Status", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_name_status.place (x=coord_x + 10, y=coord_y + 115, height=18)

    l_idinfo_side = tk.Label(root, text="BUY / SELL", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_side.place (x=coord_x + 90, y=coord_y + 35, height=18)

    l_idinfo_price = tk.Label(root, text="0000.00", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_price.place (x=coord_x + 90, y=coord_y + 55, height=18)
    
    l_idinfo_amount = tk.Label(root, text="0000.00000000", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_amount.place (x=coord_x + 90, y=coord_y + 75, height=18)

    l_idinfo_filled = tk.Label(root, text="0000.00000000", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_filled.place (x=coord_x + 90, y=coord_y + 95, height=18)

    l_idinfo_status = tk.Label(root, text="FILLED / CANCEL", font=('Courier New', 10, 'bold'), bg="#F5DA81")
    l_idinfo_status.place (x=coord_x + 90, y=coord_y + 115, height=18)

# Cancel Order 
if 1==1:

    coord_x = 560
    coord_y = 300

    # Background
    bg_order_cancel = tk.Label (root,relief="ridge", bg="#e7d7cc")
    bg_order_cancel.place (x=coord_x, y=coord_y, width=300, height=40)

    class thread_order_cancel(Thread):
        def run(self):

            if e_order_cancel.get() == "":
                return

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()
            
            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/order?"
            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            orderid = "&orderId=" + e_order_cancel.get()
            q_time = "&timestamp=" + t_str
            query = symbol + orderid + q_time

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.delete (url_rdy, headers=header)

                t_log.insert ("1.0",   "ORDER CANCELED:\n"
                                        + "ID    : " + str(r.json() ["orderId"]) + "\n"
                                        + "SIDE  : "  + r.json() ["side"] + "\n"
                                        + "PRICE : "  + str(float(r.json() ["price"])) + "\n"
                                        + "AMOUNT: " + str(float(r.json() ["origQty"])) + "\n"
                                        + "FILLED: " + str(float(r.json() ["executedQty"])) + "\n\n", "bg_cancel")


                t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")
                e_order_cancel.delete (0, "end")

                # Confirmation
                bg_order_cancel.configure (bg="green")
                time.sleep (0.2)
                bg_order_cancel.configure (bg="#e7d7cc")
            
            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <ORDER CANCEL FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def order_cancel():
        toc = thread_order_cancel()
        toc.start()

    def order_cancel_add():

        e_order_cancel.delete (0, "end")
        try:
            e_order_cancel.insert (0, e_trade_id_buy.selection_get())
        except:
            try:
                e_order_cancel.insert (0, e_trade_id_sell.selection_get())
            except:
                try:
                    e_order_cancel.insert (0, t_log.selection_get())
                except:
                    pass

    b_order_cancel = tk.Button(root, text="ID-Cancel", command=order_cancel)
    b_order_cancel.place(x=coord_x + 10 , y=coord_y + 10, width=70, height=18)

    b_order_cancel_buy = tk.Button(root, text="ADD", command=order_cancel_add)
    b_order_cancel_buy.place(x=coord_x + 90 , y=coord_y + 10, width=40, height=18)

    e_order_cancel = tk.Entry (root,font=('Courier New', 10, 'bold'))
    e_order_cancel.place (x=coord_x + 135, y=coord_y + 10, width=155, height=18)

# Show all Order from Pair
if 1==1:

    coord_x = 560
    coord_y = 350

    # Background
    bg_allorder = tk.Label (root,relief="ridge", bg="#F5DA81")
    bg_allorder.place (x=coord_x, y=coord_y, width=300, height=40)

    class thread_all_order(Thread):
        def run(self):

            # Time sync
            if e_timesync.get() == "":
                tts = thread_timesync()
                tts.start()
                tts.join()
            
            t_str = "%.0f" % (time.time() * 1000 + float(e_timesync.get()))

            base_url = "https://api.binance.com/api/v3/openOrders?"

            symbol = "symbol=" + e_main_asset1.get().upper() + e_main_asset2.get().upper()
            q_time = "&timestamp=" + t_str
            query = symbol + q_time

            signature = hmac.new(e_sk.get().encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
            sign_end = "&signature=" + signature

            url_rdy = base_url + query + sign_end
            header = {'X-MBX-APIKEY' : e_ak.get()}

            try:
                r = requests.get (url_rdy, headers=header)

                if len(r.json()) > 0: 

                    # Order count
                    l_allorder_count.configure (text=len(r.json()))   

                    for i in range (0, len(r.json())):
                        
                        # BG for order
                        if r.json() [i] ["side"] == "BUY":
                            bg_use = "bg_green"
                        else:
                            bg_use = "bg_red"

                        t_log.insert ("1.0",   "ID    : " + str(r.json() [i] ["orderId"]) + "\n"
                                             + "SIDE  : "  + r.json() [i] ["side"] + "\n"
                                             + "PRICE : "  + str(float(r.json() [i] ["price"])) + "\n"
                                             + "AMOUNT: " + str(float(r.json() [i] ["origQty"])) + "\n"
                                             + "FILLED: " + str(float(r.json() [i] ["executedQty"])) + "\n\n", bg_use)

                else:

                    # Order count
                    l_allorder_count.configure (text="00")   
                    t_log.insert ("1.0", "NO OPEN ORDER:\n" + e_main_asset1.get().upper() + "/" + e_main_asset2.get().upper() + "\n\n")

                t_log.insert ("1.0", "ALL OPEN ORDER:\n" +  e_main_asset1.get().upper() + "/" + e_main_asset2.get().upper() + "\n")
                t_log.insert ("1.0", time.strftime(" <%d.%m.%y %H:%M:%S>") + "\n\n", "bg_time")
            
                # Confirmation
                bg_allorder.configure (bg="green")
                time.sleep (0.2)
                bg_allorder.configure (bg="#F5DA81")

            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET ALL ORDER FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def all_order():
        tao = thread_all_order()
        tao.start()

    b_allorder = tk.Button (root, text="Show all open order from pair", command=all_order)
    b_allorder.place(x=coord_x + 10 , y=coord_y + 10, width=240, height=20)

    l_allorder_count = tk.Label (root, text="00", font=('Courier New', 16, 'bold'), bg="#F5DA81")
    l_allorder_count.place(x=coord_x + 255 , y=coord_y + 10, width=40, height=20)

# Time Sync
if 1==1:

    coord_x = 560
    coord_y = 400

    # Background
    bg_timesync = tk.Label (root,relief="ridge", bg="#F5DA81")
    bg_timesync.place (x=coord_x, y=coord_y, width=300, height=45)

    class thread_timesync(Thread):
        def run(self):

            try:

                r = requests.get ("https://api.binance.com/api/v1/time", timeout=4)
                
                pc_time = int(time.time() * 1000)
                servertime = int(r.json() ["serverTime"])
                diff = servertime - pc_time

                e_timesync.delete (0, "end")
                e_timesync.insert (0, diff)

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S")  + "  <TIME SYNC>\nservertime: " + str(servertime) + "\npc time:    " + str(pc_time) + "\ndiff:       " + str(diff) + "\n\n" )
                
            except Exception as e:

                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <TIME SYNC FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")

    def timesync():

        tts = thread_timesync()
        tts.start()

    b_timesync = tk.Button(root, text="Time Sync", command=timesync)
    b_timesync.place(x=coord_x + 10 , y=coord_y + 10, width=100, height=23)

    e_timesync = tk.Entry (root, font=('Courier New', 10, 'bold'))
    e_timesync.place (x=coord_x + 120, y=coord_y + 10, width=170, height=23)

# Log Textfield
if 1==1:

    coord_x = 870
    coord_y = 20

    # Background
    bg_logfield = tk.Label (root,relief="ridge", bg="#000000")
    bg_logfield.place (x=coord_x, y=coord_y, width=230, height=585)

    t_log = tk.Text (root,  font=('Courier New', 10, 'bold'))
    t_log.place(x=873, y=23, width=224, height=579)

    #BG tags for logfield
    t_log.tag_config ("bg_time", background="#d0d0d0" )
    t_log.tag_config ("bg_green", background="#d9ffd9" )
    t_log.tag_config ("bg_red", background="#ffc0cb" )
    t_log.tag_config ("bg_funds", background="#99CC99" )
    t_log.tag_config ("bg_cancel", background="#e7d7cc" )

    #Temp Textfield for load etg_binance.txt
    t_save = tk.Text (root)

# Request Textfield
if 1==1:

    t_request = tk.Text (root,  font=('Courier New', 9, 'bold'), bg="#d0d0d0")
    t_request.place(x=10, y=455, width=850, height=150)

# Time
if 1==1:

    l_time = tk.Label(root, font=('Courier New', 20, 'bold'))
    l_time.place (x=15, y=20)

    class thread_time(Thread):
        def run(self):

            global end_thread_time
            end_thread_time = 1 
            
            while end_thread_time == 1:
                try:
                    zeit = (time.strftime("%H:%M:%S"))
                    l_time.configure(text=zeit)
                    time.sleep(1)
                except:
                    pass
    
    tt = thread_time()
    tt.start()

# Keys
if 1==1:

    coord_x = 10
    coord_y = 630

    def show_keys():

        if b_keys.cget ("text") == ".":
            root.geometry ("1110x815")
            b_keys.configure (text="")
        else:
            root.geometry ("1110x615")
            b_keys.configure (text=".")

    def keys_load():

        try:
            save_file = open ("etg_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)

            if t_save.get ("11.0", "11.end") == "" or t_save.get ("12.0", "12.end") == "":
                t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <NO DATA SAVED>" + "\n\n")
                return
            
        except Exception as e:
            t_request.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <LOAD FILE FAIL>\nEXCEPTION: " + str(e) + "\n\n")
            return

        e_ak.delete (0, "end")
        e_ak.insert (0, t_save.get ("11.0", "11.end"))
        e_sk.delete (0, "end")
        e_sk.insert (0, t_save.get ("12.0", "12.end"))

    def keys_save():
    
        try:
            save_file = open ("etg_binance.txt").read()

            t_save.delete ("1.0", "end")
            t_save.insert ("1.0", save_file)
        
        except:
            t_save.delete ("1.0", "end")
            
            for i in range (1, 13):
                t_save.insert ( str(i) + ".0", "\n")

        t_save.delete ("11.0", "12.end")
        t_save.insert ("11.0", e_ak.get())
        t_save.insert ("12.0", e_sk.get())

        new_save = open ("etg_binance.txt" , "w")
        new_save.write (t_save.get("1.0", "13.0"))
        new_save.close()

    b_keys = tk.Button(root, text=".", command=show_keys)
    b_keys.place (x=0 , y=605, width=10, height=10)

    l_akey = tk.Label(root, text="A-Key:", font=('Courier New', 10, 'bold'))
    l_akey.place (x=coord_x, y=coord_y, height=20)

    l_skey = tk.Label(root, text="S-Key:", font=('Courier New', 10, 'bold'))
    l_skey.place (x=coord_x, y=coord_y + 25, height=20)

    e_ak = tk.Entry (root, font=('Courier New', 10, 'bold'))
    e_ak.place (x=coord_x + 70 , y=coord_y, width=800, height=20)

    e_sk = tk.Entry (root, font=('Courier New', 10, 'bold'))
    e_sk.place (x=coord_x + 70 , y=coord_y + 25, width=800, height=20)

    b_keys_save = tk.Button(root, text="SAVE", bg="#d0d0d0", command=keys_save)
    b_keys_save.place (x=coord_x + 880 , y=coord_y, width=50, height=18)

    b_keys_load = tk.Button(root, text="LOAD", bg="#d0d0d0", command=keys_load)
    b_keys_load.place (x=coord_x + 880 , y=coord_y + 25, width=50, height=18)

# Donation
if 1==1:

    coord_x = 10
    coord_y = 690

    def c_btc():
        root.clipboard_clear()
        root.clipboard_append(l_btc_adress.cget ("text"))
    def c_eth():
        root.clipboard_clear()
        root.clipboard_append(l_eth_adress.cget ("text"))
    def c_bnb():
        root.clipboard_clear()
        root.clipboard_append(l_bnb_adress.cget ("text"))
    def c_bch():
        root.clipboard_clear()
        root.clipboard_append(l_bch_adress.cget ("text"))
    def c_ltc():
        root.clipboard_clear()
        root.clipboard_append(l_ltc_adress.cget ("text"))

    l_donate = tk.Label (root, text="Support:", font=('Courier New', 10, 'bold'))
    l_donate.place (x=coord_x , y=coord_y, height=18)

    l_btc = tk.Label (root, text="BTC:", font=('Courier New', 10, 'bold'))
    l_btc.place (x=coord_x , y=coord_y + 25, height=18)

    l_btc_adress = tk.Label (root, text="14W14xpdy7qSQsJA8koPbLSNV7pS231Mvr", font=('Courier New', 10, 'bold'))
    l_btc_adress.place (x=coord_x + 50 , y=coord_y + 25, height=18)

    b_btc = tk.Button(root, text="Copy", font=('Courier New', 10, 'bold'), bg="#d0d0d0", command=c_btc)
    b_btc.place (x=coord_x + 480 , y=coord_y + 25, width=50, height=18)
    
    l_eth = tk.Label (root, text="ETH:", font=('Courier New', 10, 'bold'))
    l_eth.place (x=coord_x , y=coord_y + 45, height=18)

    l_eth_adress = tk.Label (root, text="0xC030B5176057fc234B73A315204d92631B649bD1", font=('Courier New', 10, 'bold'))
    l_eth_adress.place (x=coord_x + 50 , y=coord_y + 45, height=18)

    b_eth = tk.Button(root, text="Copy", font=('Courier New', 10, 'bold'), bg="#d0d0d0", command=c_eth)
    b_eth.place (x=coord_x + 480 , y=coord_y + 45, width=50, height=18)
    
    l_bnb = tk.Label (root, text="BNB:", font=('Courier New', 10, 'bold'))
    l_bnb.place (x=coord_x , y=coord_y + 65, height=18)

    l_bnb_adress = tk.Label (root, text="bnb1eezams8lr74c8tzrw2f3shnzkfl9qxw6dxf7vh", font=('Courier New', 10, 'bold'))
    l_bnb_adress.place (x=coord_x + 50 , y=coord_y + 65, height=18)

    b_bnb = tk.Button(root, text="Copy", font=('Courier New', 10, 'bold'), bg="#d0d0d0", command=c_bnb)
    b_bnb.place (x=coord_x + 480 , y=coord_y + 65, width=50, height=18)
    
    l_bch = tk.Label (root, text="BCH:", font=('Courier New', 10, 'bold'))
    l_bch.place (x=coord_x + 550 , y=coord_y + 25, height=18)
    
    l_bch_adress = tk.Label (root, text="qzh286hdvn97hrxprlr6q8sqzrxgkselnqcg890a4x", font=('Courier New', 10, 'bold'))
    l_bch_adress.place (x=coord_x + 600 , y=coord_y + 25, height=18)
    
    b_bch = tk.Button(root, text="Copy", font=('Courier New', 10, 'bold'), bg="#d0d0d0", command=c_bch)
    b_bch.place (x=coord_x + 1030 , y=coord_y + 25, width=50, height=18)
    
    l_ltc = tk.Label (root, text="LTC:", font=('Courier New', 10, 'bold'))
    l_ltc.place (x=coord_x + 550 , y=coord_y + 45, height=18)
    
    l_ltc_adress = tk.Label (root, text="LZPZ5KKb3tgoihPSEjnhbn8brggrsDEFnE", font=('Courier New', 10, 'bold'))
    l_ltc_adress.place (x=coord_x + 600 , y=coord_y + 45, height=18)
    
    b_ltc = tk.Button(root, text="Copy", font=('Courier New', 10, 'bold'), bg="#d0d0d0", command=c_ltc)
    b_ltc.place (x=coord_x + 1030 , y=coord_y + 45, width=50, height=18)

    l_telegram = tk.Label (root, text="Telegram: @Frosti_ger", font=('Courier New', 10, 'bold'))
    l_telegram.place (x=coord_x + 550 , y=coord_y + 65, height=18)

# Load Keys when saved
if 1==1:
    keys_load()

root.mainloop()
end_thread_time = 0