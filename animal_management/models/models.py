from odoo import models, fields, api


class AmAppointment(models.Model):
    _name = 'am.appointment'
    _description = 'Am Appointment'

    name = fields.Char(string='Appointment ID')
    pasien_id = fields.Many2one('product.template', string='Pasien ID')
    owner_id = fields.Many2one('res.partner', string='Owner ID')
    dokter_id = fields.Many2one('res.partner', string='Dokter Hewan ID')

    start_date = fields.Datetime(string='Tanggal Mulai')
    end_date = fields.Datetime(string='Tanggal Berakhir')
    rencana_kontrol = fields.Datetime(string='Rencana Kontrol')
    
    petugas_id = fields.Many2one('res.users', string='Petugas ID')
    email = fields.Char(string='Email', related='petugas_id.login')

    urgent = fields.Selection([('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Very High', 'Very High')],string='Urgency')
    service_ids = fields.Many2many('am.service', string='Consultation Service')
    stage_id = fields.Many2one('am.stage', string='Stage')

    description = fields.Text(string='Keterangan')

    pemeriksaan_line = fields.Char(string='Hasil Pemeriksaan')
    
    prescription_line = fields.Char(string='Prescription')
    
    quotation_line = fields.Char(string='Quotation')
    
    
class AmStage(models.Model):
    _name = 'am.stage'
    _description = 'Am Stage'
    
    name = fields.Char(string='Nama Stage')
    requirements = fields.Text(string='Reqirements') 
    sequence = fields.Integer(string='Squence')

class AmService(models.Model):
    _name = 'am.service'
    _description = 'Am Service'

    name = fields.Char(string='Service')
    color = fields.Integer(string='Warna' )