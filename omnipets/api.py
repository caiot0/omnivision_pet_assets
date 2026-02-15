import frappe

@frappe.whitelist(allow_guest=True)
def get_pet_info(pet_id):
    """
    Fetches pet information from a Customer document.
    :param pet_id: The ID of the Customer (tutor) to fetch information from.
    """
    if not frappe.db.exists("Customer", pet_id):
        frappe.throw(f"Customer not found: {pet_id}", frappe.DoesNotExistError)

    pet_info = frappe.get_doc("Customer", pet_id)

    # Assume phone number is stored in a standard field, e.g., 'phone' or 'mobile_no'
    # Check multiple common fields for phone number
    tutor_phone = pet_info.get("phone") or pet_info.get("mobile_no") or pet_info.get("custom_phone_number")

    return {
        "nome_do_pet": pet_info.custom_pet_name,
        "raca": pet_info.custom_pet_breed,
        "imagem": pet_info.custom_pet_image,
        "telefone_do_tutor": tutor_phone,
        "idade": pet_info.custom_pet_age,
        "peso": pet_info.custom_pet_weight,
        "status_de_vacinacao": pet_info.custom_vaccination_status,
        "status_de_seguranca": pet_info.custom_security_status,
        "customer_name": pet_info.customer_name
    }
