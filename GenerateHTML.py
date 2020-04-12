
class KritzelKaffeeTweet:
    def __init__(self, id, date, imglink, text, name):
         self.id = id
         self.date = date
         self.imglink = imglink
         self.text = text
         self.name = name


def convert_to_KritzelKaffeeTweet(line):
    return KritzelKaffeeTweet(line[0], line[1], line[2], line[3], line[4])

def read_csv():
    import csv
    filename = "KritzelKaffeesWithNames.csv" 
    kritzelkaffees = []
    with open(filename, 'rb', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            kritzelkaffees.append(convert_to_KritzelKaffeeTweet(row))
    return kritzelkaffees

def save_html(kritzelkaffees):
    filename = "KritzelKaffees.html"
    with open('html/'+filename, 'w', encoding="utf-8") as htmlfile:
        from HtmlTemplate import htmlstart, htmlend
        htmlfile.write(htmlstart)
        for k in kritzelkaffees:
            htmlfile.write("<tr>\n")
            htmlfile.write("<td>"+k.date+"</td>\n")
            htmlfile.write("<td>"+k.name+"</td>\n")
            htmlfile.write("<td>"+k.text+"</td>\n")
            htmlfile.write("<td><img src='"+k.imglink+"' width='200px'></td>\n")
            htmlfile.write("</tr>\n")
        htmlfile.write(htmlend)
    return filename


if __name__ == "__main__":
    print('Looking for KritzelKaffee csv file')
    kritzelkaffees = read_csv()
    print('Found ' + str(len(kritzelkaffees)) + ' KritzelKaffee entries!')
    htmlfilename = save_html(kritzelkaffees)
    print('Wrote data to ' + htmlfilename)
    print('Bye')
