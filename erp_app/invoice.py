import frappe
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

class CustomSalesInvoice(SalesInvoice):
    
    def validate(self):
        super().validate()  
        self.custom_validate()
        frappe.msgprint(f"Invoice validated for {self.customer}", indicator="green")
    
    def on_submit(self):
        super().on_submit() 
        frappe.log_error(
            title="Sales Invoice Submitted",
            message=f"Invoice {self.name} submitted for {self.customer} with total {self.grand_total}"
        )
def on_invoice_submit(doc, method):
    frappe.log_error(
        title="Sales Invoice Submitted",
        message=f"Invoice {doc.name} submitted for customer {doc.customer} with total {doc.grand_total}"
    )
    