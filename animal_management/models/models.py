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

class AmPemeriksaan(models.Model):
    _name = 'am.pemeriksaan'
    _description = 'Pemeriksaan'

    name = fields.Char(string="Pemeriksaan ID")

    appointment_id = fields.Many2one ('am.appointment', string='Appointment ID')
    pasien_id = fields.Many2one('product.template', string='Pasien ID')
    owner_id = fields.Many2one('res.partner', string='Owner ID')
    dokter_id = fields.Many2one('res.partner', string='Dokter ID')
    petugas_id = fields.Many2one('res.users', string='Petugas ID' )
    start_date = fields.Datetime(string='Tanggal Mulai',default=fields.Date.context_today)

    suhu = fields.Integer (string='Suhu')
    napas = fields.Char (string='Frekuensi Pernapasan')
    pulsus = fields.Char(string='pulsus')
    klinis = fields.Char(string='Temuan Klinis')
    terapi = fields.Char(string='Terapi')
    hidrasi = fields.Char(string='Status Hidrasi')
    prognosa = fields.Selection([('fausta', 'Fausta'), ('dubius', 'Dubius'),('infausta','Infausta')])
    diagnosa = fields.Char(string='Diagnosa')
    tindakan = fields.Char(string='Tindakan')
