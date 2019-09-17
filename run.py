import lxml.html
import requests


def scrape(url):
    html = requests.get(url)
    doc = lxml.html.fromstring(html.content)
    teams1 = []
    teams2 = []
    data = []
    for team in doc.xpath('//div[@class="tabs"]/ul[@class="staff-nav list-unstyled"]/li'):
        teams1.append({'name': team.xpath('normalize-space(./a/text())'), 'id': team.xpath('normalize-space(./a/@href)')})
    if len(teams1) ==  0:
        for team in doc.xpath('//div[@class="navLinks"]/ul[@class="nav nav-tabs nav-justified staffNav"]/li'):
            teams2.append(
                {'name': team.xpath('normalize-space(./a/text())'), 'id': team.xpath('normalize-space(./a/@href)')})
    if len(teams1) >0:
        for team in teams1:
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
    elif len(teams2) >0:
        for team in teams2:
            staffs = doc.xpath(
                '//div[@id="{}"]/div[@class="col-flush-5 span-flush-1-5 team-member-overlay"]'.format(
                    team['id'][1:]))
            for staff in staffs:
                full_name = staff.xpath('normalize-space(./a/div[@class="team-member"]/div[@class="team-meta"]/h3/text())')
                title = staff.xpath('normalize-space(./a/div[@class="team-member"]/div[@class="team-meta"]/p/text())')
                telephone = staff.xpath('normalize-space(./following-sibling::div[1]/div[@class="modal-dialog"]/div/div[@class="modal-header"]/p[@class="phone1 margin-x "]/a/text())')
                email = staff.xpath('normalize-space(./following-sibling::div[1]/div[@class="modal-dialog"]/div/div[@class="modal-header"]/p[@class="email "]/a/text())')
                staff_data = {'team': team['name'], 'full_name': full_name, 'title': title, 'telephone': telephone,
                                  'email': email}
                data.append(staff_data)
    return data


def scrape2(url):
    html = requests.get(url)
    doc = lxml.html.fromstring(html.content)
    data = []
    staffs = doc.xpath('//ul[@id="staffList"]/li/dl')
    for staff in staffs:
        full_name = staff.xpath('normalize-space(./dt[@class="fn"]/a/text())')
        title = staff.xpath('normalize-space(./dd[@class="title"]/text())')
        telephone = staff.xpath('normalize-space(./dd[@class="phone"]/text())')
        email = staff.xpath('normalize-space(./dd[@class="email"]/text())')
        staff_data = {'full_name': full_name, 'title': title, 'telephone': telephone,
                      'email': email}
        data.append(staff_data)
    return data


if __name__ == "__main__":
    result = scrape2("https://www.victorychryslerdodgejeepram.com/dealership/staff.htm")
    print(result)
    print("\n########################################")
    result = scrape("https://www.lexusoflehighvalley.com/staff.aspx")
    print(result)
    print("\n########################################")
    result = scrape("https://barrington.porschedealer.com/staff.aspx")
    print(result)
    print("\n########################################")
    result = scrape("https://www.tanskysawmilltoyota.com/staff.aspx")
    print(result)
    print("\n########################################")
    result = scrape("https://www.leithacuracary.com/staff.aspx")
    print(result)
    print("\n########################################")
    result = scrape("https://www.centralkia.com/staff.aspx")
    print(result)

