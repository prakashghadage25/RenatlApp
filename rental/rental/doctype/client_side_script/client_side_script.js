// Copyright (c) 2024, BWP and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Script", {
	// refresh : function(frm) {
    //       frappe.msgprint("Hello Frappe...")
	// }
    // after_save: function(frm){
    //     frappe.throw(" Aftre save Event ....")
        
    // }
    // enable: function(frm){
    //     frappe.msgprint("Hello frappe Enable-filed.....")
    // },
    // family_member_on_form_rendered: function(frm){
    //     frappe.msgprint("In famaily member Table")
    // }

    // after_save: function(frm){
    //     frappe.msgprint(__("The full name is '{0}'",[frm.doc.first_name+" "+frm.doc.last_name]))
    // }
    refresh:function(frm){
    frm.add_custom_button('Click Me',() => {
        frappe.msgprint(__('You clicked button'));
    })
}
});
// frappe.ui.form.on("Child table",{
       
//     age: function(frm){
//         frappe.msgprint("Interacting with child table age")
//     }
       
// });
