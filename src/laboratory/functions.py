from reservations_management.models import ReservedProducts
from laboratory.models import ShelfObject
from django.http import JsonResponse
from async_notifications.models import EmailTemplate

def return_laboratory_of_shelf_id(request):
    labs = []
    if request.method == 'GET':
        shelf_objects_ids = request.GET.getlist("ids[]")
        for shelf_objects_id in shelf_objects_ids:
            lab_id_queryset = ShelfObject.objects.filter(id=shelf_objects_id).values('shelf__furniture__labroom__laboratory__id')
            for lab_id in lab_id_queryset:
                labs.append(lab_id['shelf__furniture__labroom__laboratory__id'])
        return JsonResponse({'lab_ids': labs})


def f():
    template = EmailTemplate.objects.filter(code='Shelf object in limit').first()
    if template is not None:
        temp = "<p>Hola</p><p>&nbsp;</p><p>Usted ha recibido este correo porque tiene un cambio en un laboratorio en el sistema Organilab.</p>" \
               "<p>&nbsp;</p><p>Este mensaje es para notificarle que uno o m&aacute;s objetos en el laboratorio <strong>{{ laboratory.name }}</strong> est&aacute;n en las cuotas m&iacute;nimas.</p>" \
               "<h4>Detalle de productos</h4>" \
               "<p>{% for obj in shelf_object %}</p><p><strong>Estante:</strong> {{ obj.shelf }} <strong>Objeto:</strong> {{ obj.object }} <strong>Cantidad de material:</strong> {{ obj.quantity }} <strong>Cantidad l&iacute;mite de material:</strong> {{ obj.limit_quantity }} <strong>Unidad de medida:</strong> {{ obj.measurement_unit }}</p>" \
               "<p><a href='{{ blockurl }}{{ obj.pk }}'>{{ blockurl }}{{ obj.pk }}</a></p><p>{% endfor %}</p><p>&nbsp;</p><p>&nbsp;</p>" \
               "<p>&nbsp;</p><p>&nbsp;</p>" \
               "<p>Por favor recargue este producto o contacte a la persona que pueda hacerlo.</p>" \
               "<p><br />Gracias,<br /><br />Organilab: Reporte de objetos</p><p>&nbsp;</p>" \
               "<p>&nbsp;</p>"
        template.message = temp
        template.save()