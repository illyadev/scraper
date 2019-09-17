import lxml.html
import requests


def scrape(url):
    html = requests.get(url)
    doc = lxml.html.fromstring(html.content)
    teams = []
    data = []
    for team in doc.xpath('//div[@class="tabs"]/ul[@class="staff-nav list-unstyled"]/li'):
        teams.append({'name': team.xpath('normalize-space(./a/text())'), 'id': team.xpath('normalize-space(./a/@href)')})
    if len(teams) > 0:
        for team in teams:
            staffs = doc.xpath(
                '//div[@id="{}"]/div/div/div/div/div[@class="staff-info col-sm-7 col-xs-9 col-xxs-8 pad-left-x"]'.format(
                    team['id'][1:]))
            for staff in staffs:
                full_name = staff.xpath('normalize-space(./div[@class="staff-title h3 margin-top-x"]/text())')
                title = staff.xpath('normalize-space(./div[@class="staff-desc margin-bottom_5x"]/em/text())')
                telephone = staff.xpath('normalize-space(./div/a[@title="Phone"]/@href)')
                if len(telephone) > 0:
                    telephone = telephone[4:]
                email = staff.xpath('normalize-space(./div/a[@title="Email"]/@href)')
                if len(email) > 0:
                    email = email[7:]
                    staff_data = {'team': team['name'], 'full_name': full_name, 'title': title, 'telephone': telephone,
                                  'email': email}
                data.append(staff_data)
    else:
        staffs = doc.xpath('//ul[@id="staffList"]/li/dl')
        for staff in staffs:
            full_name = staff.xpath('normalize-space(./dt[@class="fn"]/a/text())')
            title = staff.xpath('normalize-space(./dd[@class="title"]/text())')
            telephone =  staff.xpath('normalize-space(./dd[@class="phone"]/text())')
            email = staff.xpath('normalize-space(./dd[@class="email"]/text())')
            staff_data = { 'full_name': full_name, 'title': title, 'telephone': telephone,
                              'email': email}
            data.append(staff_data)
    return data



if __name__ == "__main__":
    result = scrape("https://www.victorychryslerdodgejeepram.com/dealership/staff.htm")
    print(result)
    # result = scrape("https://barrington.porschedealer.com/staff.aspx")
    # print(result)
    # result = scrape("https://www.tanskysawmilltoyota.com/staff.aspx")
    # print(result)
    # result = scrape("https://www.leithacuracary.com/staff.aspx")
    # print(result)
