import json
import os

def load_data(file_name):
    path = os.path.join("data", file_name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

company_info = load_data("company.json")
services_info = load_data("services.json")
estimator_info = load_data("estimator.json")
testimonials_info = load_data("testimonials.json")
contact_info = load_data("contact.json")
internship_info = load_data("internships.json")

def generate_response(user_input):
    user_input = user_input.lower()

    if "about" in user_input or "company" in user_input:
        return company_info.get("about", "No info found.")

    if "mission" in user_input:
        return company_info.get("mission", "No mission info available.")

    if "vision" in user_input:
        return company_info.get("vision", "No vision info available.")

    if "value" in user_input:
        return "\n".join(company_info.get("values", []))

    if "why choose" in user_input or "why us" in user_input:
        return "\n".join(company_info.get("why_choose_us", []))

    if "service" in user_input:
        return "We offer: " + ", ".join(services_info.keys())

    for service, description in services_info.items():
        if service.lower() in user_input:
            return description

    if any(keyword in user_input for keyword in ["estimate", "pricing", "cost"]):
        return json.dumps(estimator_info, indent=2)

    if "testimonial" in user_input:
        return "\n".join(testimonials_info.get("testimonials", []))

    if "contact" in user_input:
        return f"""📧 Email: {contact_info['email']}
📞 Phone: {contact_info['phone']}
💬 WhatsApp: {contact_info['whatsapp']}
📍 Location: {contact_info['location']}"""

    if "internship" in user_input:
        return "\n".join(internship_info.get("available_roles", []))

    return "I'm here to help with anything about Techverra Solutions. You can ask about services, internships, pricing, or how to contact us!"
