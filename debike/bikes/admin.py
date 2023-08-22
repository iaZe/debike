from django.contrib import admin
from .models import Bike, Venda, Historico

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ("ID", "codigo", "modelo", "cor", "dono", "restricao", "data_cadastro")
    list_filter = ("restricao", "data_cadastro")
    search_fields = ("codigo", "modelo", "cor", "dono__username")
    readonly_fields = ("data_cadastro",)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ("ID", "bike", "comprador", "valor", "data_venda")
    list_filter = ("data_venda",)
    search_fields = ("bike__codigo", "bike__modelo", "bike__cor", "bike__dono__username", "comprador__username")
    readonly_fields = ("data_venda",)

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ("bike", "data_atualizacao")
    list_filter = ("data_atualizacao",)
    search_fields = ("bike__codigo", "bike__modelo", "bike__cor", "bike__dono__username")
    readonly_fields = ("data_atualizacao",)

    
