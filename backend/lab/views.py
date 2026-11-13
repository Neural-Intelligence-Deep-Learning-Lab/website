from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "lab/home.html"


class AdvisorView(TemplateView):
    template_name = "lab/advisor.html"


class PublicationsView(TemplateView):
    template_name = "lab/publications.html"


class PublicationDetailView(TemplateView):
    template_name = "lab/publication_detail.html"


class TeamView(TemplateView):
    template_name = "lab/team.html"
