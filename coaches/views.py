from django.views.generic.detail import DetailView
from coaches.models import Coach

class MixinCoachContext(object):
    def get_context_data(self, **kwargs):
        context = super(MixinCoachContext, self).get_context_data(**kwargs)
        coach = self.get_object()
        context['title'] = "%s %s" % (coach.first_name_field(), coach.last_name_field())
        return context	
 
class CoachDetailView(MixinCoachContext, DetailView):
    model = Coach
    template_name = 'coaches/detail.html'
 