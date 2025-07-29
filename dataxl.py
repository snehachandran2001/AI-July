import xlsxwriter

data = [
    {
        "name": "John Doe",
        "phone": "+1-202-555-0176",
        "email": "john.doe@example.com",
        "address": "123 Main Street, New York, NY",
        "country": "USA"
    },
    {
        "name": "Emma Smith",
        "phone": "+44-7911-123456",
        "email": "emma.smith@example.co.uk",
        "address": "45 Queen's Road, London",
        "country": "UK"
    },
    {
        "name": "Raj Kumar",
        "phone": "+91-9876543210",
        "email": "raj.kumar@example.in",
        "address": "12 MG Road, Mumbai",
        "country": "India"
    },
    {
        "name": "Sophia Lopez",
        "phone": "+61-412-345-678",
        "email": "sophia.lopez@example.com.au",
        "address": "78 George Street, Sydney",
        "country": "Australia"
    },
    {
        "name": "Carlos Rivera",
        "phone": "+52-55-1234-5678",
        "email": "carlos.rivera@example.mx",
        "address": "Av. Reforma 123, Mexico City",
        "country": "Mexico"
    }
]


workbook = xlsxwriter.Workbook('dataxl.xlsx')
worksheet = workbook.add_worksheet("first_sheet")

worksheet.write(0, 0, "#")
worksheet.write(0, 1, "Name")
worksheet.write(0, 2, "Phone")
worksheet.write(0, 3, "Email")
worksheet.write(0, 4, "Address")
worksheet.write(0, 5, "Country")

for index, entry in enumerate(data, start=1):
    worksheet.write(index+1, 0, str(index))
    worksheet.write(index+1, 1, entry["name"])
    worksheet.write(index+1, 2, entry["phone"])
    worksheet.write(index+1, 3, entry["email"])
    worksheet.write(index+1, 3, entry["address"])
    worksheet.write(index+1, 4, entry["country"])

workbook.close()