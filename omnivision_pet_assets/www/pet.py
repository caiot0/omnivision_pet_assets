import frappe

def get_context(context):
    # You can add any context variables here that you want to pass to the template
    # For example, get the pet_id from the query string
    context.pet_id = frappe.form_dict.get("name")
    
    if not context.pet_id:
        # Handle case where pet_id is not provided, maybe show a search page or an error
        context.no_pet_id = True
        return

    # The actual data loading will be done via JS, 
    # but you could pass initial data if needed.
    # For now, just passing the pet_id is enough.
    pass
