# myapp/services/queries.py

from myapp.models import FAQ

class FAQQueryService:
    @staticmethod
    def get_faq_by_id(faq_id):
        try:
            return FAQ.objects.get(id=faq_id)
        except FAQ.DoesNotExist:
            return None

    @staticmethod
    def list_all_faqs():
        return FAQ.objects.all()
