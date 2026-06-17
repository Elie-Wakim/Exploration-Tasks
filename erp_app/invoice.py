from apps.erpnext.erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice

import frappe

class CustomSalesInvoice(SalesInvoice):
    
    def validate(self):
        super().validate()  
        frappe.msgprint(f"Invoice validated for {self.customer}", indicator="green")
    
def on_invoice_submit(doc, method):
    frappe.log_error(
        title="Sales Invoice Submitted",
        message=f"Invoice {doc.name} submitted for customer {doc.customer} with total {doc.grand_total}"
    )
    