#MOVIE TICKET BOOKING SYSTEM
def seat_arrangement():
    A=ord("H")
    for I in range(8):
        if I==0 or I==1:
            print(chr(A),"---",end=" ")
            for J in range(1,11):
                print(J,end=" ")
            print()
            A=ord(chr(A))-1
        else:
            print(chr(A),"---",end="   ")
            for K in range (1,9):
                print(K,end=" ")
            print()
            A=ord(chr(A))-1

List1=[{"movie":"Avengers","price":250,"theatre":1},{"movie":"Conjuring","price":180,"theatre":2},{"movie":"Interstellar","price":200,"theatre":3},{"movie":"The Lion King","price":190,"theatre":4},{"movie":"The Jungle Book","price":210,"theatre":5}]
T1=[["A1","A2","A3","A4","A5","A6","A7","A8"],["B1","B2","B3","B4","B5","B6","B7","B8"],["C1","C2","C3","C4","C5","C6","C7","C8"],["D1","D2","D3","D4","D5","D6","D7","D8"],
    ["E1","E2","E3","E4","E5","E6","E7","E8"],["F1","F2","F3","F4","F5","F6","F7","F8"],["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10"],
    ["H1","H2","H3","H4","H5","H6","H7","H8","H9","H10"]]
T2=[i.copy() for i in T1]
T3=[i.copy() for i in T1]
T4=[i.copy() for i in T1]
T5=[i.copy() for i in T1]
print("Hello!! Let's give you a smooth movie booking experience")
print("Movies available:")
print("Avengers")
print("Conjuring")
print("Interstellar")
print("The Lion King")
print("The Jungle Book")
booking=False
while booking==False:
    choice=input("Enter the movie you want to watch:").strip()
    if choice.upper()=="AVENGERS":
        booking=True
        print("Ticket price:",List1[0]["price"])
        print("Seats arrangement")
        seat_arrangement()
        n=int(input("How many tickets do you want to book?"))
        count=0
        while count!=n:
             print("Seats available:",T1)
             seat=input("Choose the seat of your choice out of the ones available:").upper()
             for j in range(0,8):
                 if seat in T1[j]:
                     print("Seat Booked")
                     T1[j].remove(seat)
                     count=count+1
                     break
             else:
                print("Sorry this seat is not available")
        total_price=List1[0]["price"]*n
        print("Your total ticket price will be=",total_price)
    elif choice.upper()=="CONJURING":
        booking=True
        print("Ticket price:",List1[1]["price"])
        print("Seats arrangement")
        seat_arrangement()
        print("Seats available:",T2)
        n=int(input("How many tickets do you want to book?"))
        count=0
        while count!=n:
             print("Seats available:",T2)
             seat=input("Choose the seat of your choice out of the ones available:").upper()
             for j in range(0,8):
                 if seat in T2[j]:
                     print("Seat Booked")
                     T2[j].remove(seat)
                     count=count+1
                     break
             else:
                print("Sorry this seat is not available")
        total_price=List1[1]["price"]*n
        print("Your total ticket price will be=",total_price)
    elif choice.upper()=="INTERSTELLAR":
        booking=True
        print("Ticket price:",List1[2]["price"])
        print("Seats arrangement")
        seat_arrangement()
        print("Seats available:",T3)
        n=int(input("How many tickets do you want to book?"))
        count=0
        while count!=n:
             print("Seats available:",T3)
             seat=input("Choose the seat of your choice out of the ones available:").upper()
             for j in range(0,8):
                 if seat in T3[j]:
                     print("Seat Booked")
                     T3[j].remove(seat)
                     count=count+1
                     break
             else:
                print("Sorry this seat is not available")
        total_price=List1[2]["price"]*n
        print("Your total ticket price will be=",total_price)
    elif choice.upper()=="THE LION KING":
        booking=True
        print("Ticket price:",List1[3]["price"])
        print("Seats arrangement")
        seat_arrangement()
        print("Seats available:",T4)
        n=int(input("How many tickets do you want to book?"))
        count=0
        while count!=n:
             print("Seats available:",T4)
             seat=input("Choose the seat of your choice out of the ones available:").upper()
             for j in range(0,8):
                 if seat in T4[j]:
                     print("Seat Booked")
                     T4[j].remove(seat)
                     count=count+1
                     break
             else:
                print("Sorry this seat is not available")
        total_price=List1[3]["price"]*n
        print("Your total ticket price will be=",total_price)
    elif choice.upper()=="THE JUNGLE BOOK":
        booking=True
        print("Ticket price:",List1[4]["price"])
        print("Seats arrangement")
        seat_arrangement()
        print("Seats available:",T5)
        n=int(input("How many tickets do you want to book?"))
        count=0
        while count!=n:
             print("Seats available:",T5)
             seat=input("Choose the seat of your choice out of the ones available:").upper()
             for j in range(0,8):
                 if seat in T5[j]:
                     print("Seat Booked")
                     T5[j].remove(seat)
                     count=count+1
                     break
             else:
                print("Sorry this seat is not available")
        total_price=List1[4]["price"]*n
        print("Your total ticket price will be=",total_price)
    else:
        print("Sorry! This movie is not available. Choose from the ones available")
a=input("Would you like to order some snacks as well?(Y/N)")
if a=="Y":
    print("Choose your desired snack:")
    print("101:Popcorn----(70 rupees)")
    print("102:French Fries----(60 rupees)")
    print("103:Chips-----(50 rupees)")
    print("104:Cold drinks----(40 rupees)")
    print("105:Cookies------(55 rupees)")
    food_dict={101:{"item":"Popcorn","price":70},102:{"item":"French fries","price":60},103:{"item":"Chips","price":50},
               104:{"item":"Cold drink","price":40},105:{"item":"Cookies","price":55}}
    b="Y"
    food_price=0
    while b=="Y":
        order_id=int(input("Enter the order id of your snack:"))
        quantity=int(input("Enter quantity:"))
        food_price=food_price+food_dict[order_id]["price"]*quantity
        b=input("Do you want to order anything else:(Y/N)")
    print("The total price of your snacks will be:",food_price)
    grand_total=total_price+food_price
    print("Your total bill is:",grand_total)
    print("OK! Have fun at the movies")
else:
    print("Your total bill is:",total_price)
    print("OK! Have fun at the movies")

            
                 
            
                 


            
                 
                        
                 
            
         

