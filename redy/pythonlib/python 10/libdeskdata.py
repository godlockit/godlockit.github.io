class DataProcessor:

    def format_phone_number(phone_number):
        ph = phone_number.split()

        return f"+7 ({ph[1],ph[2],ph[3]}) {ph[4],ph[5],ph[6]} {ph[7],ph[8]}-{ph[9],ph[10]}"


    def format_name(name):
        #ФИО
        name.split(".")
        if i in len(name):
            namep = name[0]
            surname= name[1]
            otchestvo= name[2]
            if name
        pass


    def calculate_discounted_price(price, discount):
        if not discount:
            discount = price/100*discount + price
        return discount