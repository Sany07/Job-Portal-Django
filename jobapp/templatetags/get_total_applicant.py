from django import template
register = template.Library()


@register.simple_tag(name='get_total_applicant')
def get_total_applicant(total_applicants , job):

    return total_applicants[job.id]
  
     



        

