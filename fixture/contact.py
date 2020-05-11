from model.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.second_name)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("home").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select first group
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(name = text, id = id))
        return contacts

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath("//img[@title='Edit']")[index].click()
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.second_name)
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def change_field_value(self, filld_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(filld_name).click()
            wd.find_element_by_name(filld_name).clear()
            wd.find_element_by_name(filld_name).send_keys(text)