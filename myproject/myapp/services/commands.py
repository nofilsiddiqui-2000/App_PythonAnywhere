# myapp/services/commands.py

from myapp.models import FAQ

class FAQCommandService:
    @staticmethod
    def create_faq(question, answer, submitted_by):
        faq = FAQ.objects.create(question=question, answer=answer, submitted_by=submitted_by)
        return faq

    @staticmethod
    def update_faq(faq_id, question=None, answer=None):
        try:
            faq = FAQ.objects.get(id=faq_id)
            if question:
                faq.question = question
            if answer:
                faq.answer = answer
            faq.save()
            return faq
        except FAQ.DoesNotExist:
            return None

    @staticmethod
    def delete_faq(faq_id):
        try:
            faq = FAQ.objects.get(id=faq_id)
            faq.delete()
            return True
        except FAQ.DoesNotExist:
            return False
