# Copyright (c) 2024, BWP and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _



class ServerSideScript(Document):
    # def validate(self):
    #     frappe.msgprint("Hello frappe")

    # def after_insert(self):
    #     frappe.msgprint("Event Occured After insert")

    # def validate(self):
    #     frappe.msgprint(_("Full Name fetched from frappe is '{0}' ").format(self.first_name+" "+self.last_name))
    
    # def validate(self):
    #     self.new_document()

    # def new_document(self):
    #     doc=frappe.new_doc('Client Side Script')
    #     doc.first_name="jay"
    #     doc.last_name="ss"
    #     doc.email="fdshga"
    #     doc.append('child_table',{ "name1":"jaya",
    #                                 "age":21,
    #                                 "relation":"son"})
    #     doc.insert()

    def validate(self):
        self.delete_doc()
    
    def delete_doc(self):
        doc=frappe.get_doc("Client Side Script", "PR-002")
        frappe.msgprint("Action Taken....")
        doc.db_set("last_name","nawro")
    
    

  