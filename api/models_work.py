# cython:language_level=3
from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _

class RustDeskToken(models.Model):
    ''' Token
    '''
    username = models.CharField(verbose_name=_('用户名'), max_length=20)
    rid = models.CharField(verbose_name=_('RustDesk ID'), max_length=16)
    uid = models.CharField(verbose_name=_('用户ID'), max_length=16)
    uuid = models.CharField(verbose_name=_('uuid'), max_length=60)
    access_token = models.CharField(verbose_name=_('access_token'), max_length=60, blank=True)
    create_time = models.DateTimeField(verbose_name=_('登录时间'), auto_now_add=True)
    #expire_time = models.DateTimeField(verbose_name='过期时间')
    class Meta:
        ordering = ('-username',)
        verbose_name = "Token"
        verbose_name_plural = _("Token列表") 

class ConnLog(models.Model):
    id = models.IntegerField(verbose_name=_('ID'),primary_key=True)
    action = models.CharField(verbose_name=_('Action'), max_length=20, null=True)
    conn_id = models.CharField(verbose_name=_('Connection ID'), max_length=10, null=True)
    from_ip = models.CharField(verbose_name=_('From IP'), max_length=30, null=True)
    rid = models.CharField(verbose_name=_('To ID'), max_length=20, null=True)
    logged_at = models.CharField(verbose_name=_('Logged At'), max_length=25, null=True)
    session_id = models.CharField(verbose_name=_('Session ID'), max_length=60, null=True)
    uuid = models.CharField(verbose_name=_('uuid'), max_length=60, null=True)

class ConnLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'action', 'conn_id', 'from_ip', 'rid', 'logged_at', 'session_id', 'uuid')
    search_fields = ('from_ip', 'rid')
    list_filter = ('id', 'from_ip', 'rid', 'logged_at')

class RustDeskTokenAdmin(admin.ModelAdmin):
    list_display = ('username', 'uid')
    search_fields = ('username', 'uid')
    list_filter = ('create_time', ) #filter
    

class RustDeskTag(models.Model):
    ''' Tags
    '''
    uid = models.CharField(verbose_name=_('所属用户ID'), max_length=16)
    tag_name = models.CharField(verbose_name=_('标签名称'), max_length=60)
    tag_color = models.CharField(verbose_name=_('标签颜色'), max_length=60, blank=True)
    
    class Meta:
        ordering = ('-uid',)
        verbose_name = "Tags"
        verbose_name_plural = _("Tags列表")

class RustDeskTagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'uid', 'tag_color')
    search_fields = ('tag_name', 'uid')
    list_filter = ('uid', )
    

class RustDeskPeer(models.Model):
    ''' Pees
    '''
    uid = models.CharField(verbose_name=_('用户ID'), max_length=16)
    rid = models.CharField(verbose_name=_('客户端ID'), max_length=60)
    username = models.CharField(verbose_name=_('系统用户名'), max_length=20)
    hostname = models.CharField(verbose_name=_('操作系统名'), max_length=30)
    alias = models.CharField(verbose_name=_('别名'), max_length=30)
    platform = models.CharField(verbose_name=_('平台'), max_length=30)
    tags = models.CharField(verbose_name=_('标签'), max_length=30)
    rhash = models.CharField(verbose_name=_('设备链接密码'), max_length=60)
    ip = models.CharField(verbose_name=_('IP Address'), max_length=16, default="")
    
    class Meta:
        ordering = ('-username',)
        verbose_name = "Peers"
        verbose_name_plural = _("Peers列表" )
        

class RustDeskPeerAdmin(admin.ModelAdmin):
    list_display = ('rid', 'uid', 'username', 'hostname', 'platform', 'alias', 'tags', 'ip')
    search_fields = ('deviceid', 'alias')
    list_filter = ('rid', 'uid', )
    
    
class RustDesDevice(models.Model):
    rid = models.CharField(verbose_name=_('客户端ID'), max_length=60, blank=True)
    cpu = models.CharField(verbose_name='CPU', max_length=100)
    hostname = models.CharField(verbose_name=_('主机名'), max_length=100)
    memory = models.CharField(verbose_name=_('内存'), max_length=100)
    os = models.CharField(verbose_name=_('操作系统'), max_length=100)
    uuid = models.CharField(verbose_name='uuid', max_length=100)
    username = models.CharField(verbose_name=_('系统用户名'), max_length=100, blank=True)
    version = models.CharField(verbose_name=_('客户端版本'), max_length=100)
    create_time = models.DateTimeField(verbose_name=_('设备注册时间'), auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=('设备更新时间'), auto_now=True, blank=True)
    ip = models.CharField(verbose_name=_('IP Address'), max_length=16, default="")
    
    class Meta:
        ordering = ('-rid',)
        verbose_name = _("设备")
        verbose_name_plural = _("设备列表" )
    
class RustDesDeviceAdmin(admin.ModelAdmin):
    list_display = ('rid', 'hostname', 'memory', 'uuid', 'version', 'create_time', 'update_time', 'ip')
    search_fields = ('hostname', 'memory')
    list_filter = ('rid', )



class ShareLink(models.Model):
    ''' Share link
    '''
    uid = models.CharField(verbose_name=_('用户ID'), max_length=16)
    shash = models.CharField(verbose_name=_('链接Key'), max_length=60)
    peers = models.CharField(verbose_name=_('机器ID列表'), max_length=20)
    is_used = models.BooleanField(verbose_name=_('是否使用'), default=False)
    is_expired = models.BooleanField(verbose_name=_('是否过期'), default=False)
    create_time = models.DateTimeField(verbose_name=_('生成时间'), auto_now_add=True)
    

    
    class Meta:
        ordering = ('-create_time',)
        verbose_name = _("分享链接")
        verbose_name_plural = _("链接列表" )
        

class ShareLinkAdmin(admin.ModelAdmin):
    list_display = ('shash', 'uid', 'peers', 'is_used', 'is_expired', 'create_time')
    search_fields = ('peers', )
    list_filter = ('is_used', 'uid', 'is_expired' )