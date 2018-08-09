from dispositivo.models import Dispositivo

class DispositivoClass():
    def get_list_dados_all(self):
        dispositivos = Dispositivo.objects.all().filter(uso=False)
        list_dic_dispositivos = []
        for d in dispositivos:
            dic_dispositivos = {}
            dic_dispositivos['nome'] = d.nome
            dic_dispositivos['codigo'] = d.codigo
            list_dic_dispositivos.append(dic_dispositivos)

        context = { 'dispositivos': list_dic_dispositivos}
        return context
