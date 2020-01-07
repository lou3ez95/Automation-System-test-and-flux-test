#!/usr/bin/python
import json
import sys
def compare(data,CPU_MAX,RAM_MAX,STORAGE_MAX,patern,indice):
        ram= int(data['Memory'])
        cpu_core= int(data['CPU']['CPU_CORES'])
        #storage= int(data['MountPoint'][0]['taille'])
        swap = float(data['Swap'])
        SWAP = float(ram)/2
        if ram < '0.512':
                print ('false')
        else:
                print ('true')
        print(ram,cpu_core)
        storage = 0
        for c in data['MountPoint']:
		if indice == "SFR" or indice == "RSR":
                        if c['Type'] == 'ntfs':
                                storage = storage + float(c['taille'])
		
		if indice == "UAR" or indice == "PRR" or indice == "LBR":
                        if c['Type'] == 'ntfs':
                                storage = storage + float(c['taille'])
                       
                if indice == "WSO":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/prd':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])

                if indice == "DBO":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/run':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/bin':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/images':
                                storage = storage + float(c['taille'])

                if indice == "CDBO":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/prd':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/bin':
                                storage = storage + float(c['taille'])

                if indice == "APLO":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/prd':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/data':
                                storage = storage + float(c['taille'])

                if indice == "APIO":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/prd':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/data':
                                storage = storage + float(c['taille'])

                if indice == "UAR":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/prd':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/data':
                                storage = storage + float(c['taille'])

                if indice == "OAMRO":
                        if c['Mount_Point'] == '/':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/boot':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/bin':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/tmp':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/var':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/home':
                                storage = storage + float(c['taille'])
                        if c['Mount_Point'] == '/usr':
                                storage = storage + float(c['taille'])

        storage = float('%.0f' % storage)
        data['local_storage'] = int(storage)
        data['detail'] = ''
        error = 0

        if cpu_core < CPU_MAX:
                error = error + 1
                data['status'] = 'NOT OK'
                data['detail'] = 'the nbr of core is less than %s ,'% CPU_MAX

        if ram < RAM_MAX:
                error = error + 1
                data['status'] = 'NOT OK'
                data['detail'] = data['detail'] + 'memory less than %sGb,' % RAM_MAX

        if storage < STORAGE_MAX:
                error = error + 1
                data['status'] = 'NOT OK'
                data['detail'] = data['detail'] + 'STORAGE less than %sG,' % STORAGE_MAX

        if swap < SWAP:
                error = error + 1
                data['status'] = 'NOT OK'
                data['detail'] = data['detail'] + 'swap less than 50% of Memory,'

        for i in data['MountPoint']:
                if patern == 'small':
                        if indice == 'WSO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/webdata':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webdata not good,'

                                if i['Mount_Point'] == '/webbackup':
                                        if i['taille'] != 85:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webbackup not good,'

                        if indice == "DBO":
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != "5":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /bin not good,'

                                if i['Mount_Point'] == '/image':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /image not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 800:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/myqdata/backup':
                                        if i['taille'] != 425:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/backup not good,'

                        if indice == 'APLO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 68:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 127:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'APIO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 157:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 213:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'UAR':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 179:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                        if indice == 'OAMRO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.100":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/usr':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /usr not good'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 50:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 70:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/oamappbackup':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamappbackup not good,'

                                if i['Mount_Point'] == '/oamdbbackup':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamdbbackup not good,'

                elif patern == 'medium':
                        if indice == 'WSO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/webdata':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webdata not good,'

                                if i['Mount_Point'] == '/webbackup':
                                        if i['taille'] != 85:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webbackup not good,'

                        if indice == "DBO":
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != "5":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /bin not good,'

                                if i['Mount_Point'] == '/images':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /image not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 900:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/myqdata/backup':
                                        if i['taille'] != 475:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/backup not good,'

                        if indice == 'APLO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 75:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 142:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'APIO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 175:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 238:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'UAR':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 179:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                        if indice == 'OAMRO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.100":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/usr':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /usr not good'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 50:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 70:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/oamappbackup':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamappbackup not good,'

                                if i['Mount_Point'] == '/oamdbbackup':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamdbbackup not good,'

                elif patern == 'high':
                        if indice == 'WSO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/webdata':
                                        if i['taille'] != 200:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webdata not good,'

                                if i['Mount_Point'] == '/webbackup':
                                        if i['taille'] != 100:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webbackup not good,'

                        if indice == "DBO":
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != "5":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /bin not good,'

                                if i['Mount_Point'] == '/images':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /image not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 500:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/myqdata/backup':
                                        if i['taille'] != 350:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/backup not good,'

                        if indice == "CDBO":
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != "5":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /bin not good,'

                                if i['Mount_Point'] == '/columnardata':
                                        if i['taille'] != 800:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /columnardata not good,'

                                if i['Mount_Point'] == '/columnarbackup':
                                        if i['taille'] != 450:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /columnarbackup not good,'

                        if indice == 'APLO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 300:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'APIO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 275:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 500:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'UAR':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 179:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                        if indice == 'OAMRO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.100":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/usr':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /usr not good'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/oamappbackup':
                                        if i['taille'] != 50:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamappbackup not good,'

                                if i['Mount_Point'] == '/oamdbbackup':
                                        if i['taille'] != 75:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamdbbackup not good,'

                else:
                        if indice == 'WSO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/webdata':
                                        if i['taille'] != 200:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webdata not good,'

                                if i['Mount_Point'] == '/webbackup':
                                        if i['taille'] != 100:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /webbackup not good,'

                        if indice == "DBO":
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != "5":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /bin not good,'

                                if i['Mount_Point'] == '/images':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /image not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 800:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/myqdata/backup':
                                        if i['taille'] != 400:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/backup not good,'

                        if indice == "CDBO":
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != "5":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /bin not good,'

                                if i['Mount_Point'] == '/columnardata':
                                        if i['taille'] != 1150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /columnardata not good,'

                                if i['Mount_Point'] == '/columnarbackup':
                                        if i['taille'] != 600:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /columnarbackup not good,'

                        if indice == 'APLO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 225:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 300:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'APIO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                                if i['Mount_Point'] == '/appdata':
                                        if i['taille'] != 525:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appdata not good,'

                                if i['Mount_Point'] == '/appbackup':
                                        if i['taille'] != 500:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /appbackup not good,'

                        if indice == 'UAR':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.512":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good,'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good,'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good,'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good,'

                                if i['Mount_Point'] == '/data':
                                        if i['taille'] != 179:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good,'

                        if indice == 'OAMRO':
                                if i['Mount_Point'] == '/':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of / not good,'

                                if i['Mount_Point'] == '/boot':
                                        if i['taille'] != "0.100":
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /boot not good,'

                                if i['Mount_Point'] == '/usr':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /usr not good'

                                if i['Mount_Point'] == '/tmp':
                                        if i['taille'] != 5:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /tmp not good'

                                if i['Mount_Point'] == '/var':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /var not good'

                                if i['Mount_Point'] == '/home':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /home not good'

                                if i['Mount_Point'] == '/bin':
                                        if i['taille'] != 10:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /data not good'

                                if i['Mount_Point'] == '/prd':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /prd not good'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/data':
                                        if i['taille'] != 150:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/data not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/log':
                                        if i['taille'] != 30:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/log not good,'

                                if i['Mount_Point'] == '/myqdata/mysrvrms/tmp':
                                        if i['taille'] != 20:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /myqdata/mysrvrms/tmp not good,'

                                if i['Mount_Point'] == '/oamappbackup':
                                        if i['taille'] != 50:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamappbackup not good,'

                                if i['Mount_Point'] == '/oamdbbackup':
                                        if i['taille'] != 75:
                                                error = error + 1
                                                data['status'] = 'NOT OK'
                                                data['detail'] = data['detail'] + 'size of /oamdbbackup not good,'
        if error != 0:
                data['detail'] = data['detail'][:-1]
        else:
                data['status'] = 'OK'
                del data['detail']

        data['patern'] = patern

        return data

def result(data,patern):
        hostname = data['Hostname']
        d = hostname[:3]
        d = d.upper()

        if d == 'OPR':
                ch = hostname[7:-4]
		ch = ch.upper()
        else:
                ch = d
        
        if patern == 'small':
                if ch == "WSO" or ch == "APLO" or ch == "APIO" or ch == "OAMRO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "PRR" or ch == "LBR":
                        data = compare(data,2,2,40,patern,ch)
                if ch == "DBO":
                        data = compare(data,2,3,50,patern,ch)

                if ch == "SFR":
                        data = compare(data,1,0.512,10,patern,ch)

                if ch == "RSR":
                        data = compare(data,1,1,8,patern,ch)

                if ch == "UAR":
                        data = compare(data,2,2,250,patern,ch)

        elif patern == 'medium':
                if ch == "WSO" or ch == "APLO" or ch == "APIO" or ch == "OAMRO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "PRR" or ch == "LBR":
                        data = compare(data,2,2,40,patern,ch)

                if ch == "DBO":
                        data = compare(data,2,4,50,patern,ch)

                if ch == "SFR":
                        data = compare(data,1,0.512,10,patern,ch)

                if ch == "RSR":
                        data = compare(data,1,1,8,patern,ch)

                if ch == "UAR":
                        data = compare(data,2,2,250,patern,ch)

        elif patern == 'high':
                if ch == "WSO" or ch == "APLO" or ch == "APIO" or ch == "OAMRO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "PRR" or ch == "LBR":
                        data = compare(data,2,2,40,patern,ch)

                if ch == "DBO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "CDBO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "SFR":
                        data = compare(data,1,0.512,10,patern,ch)

                if ch == "RSR":
                        data = compare(data,1,1,8,patern,ch)

                if ch == "UAR":
                        data = compare(data,2,2,250,patern,ch)

        else:
                if ch == "WSO" or ch == "APLO" or ch == "APIO" or ch == "OAMRO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "PRR" or ch == "LBR":
                        data = compare(data,2,2,40,patern,ch)

                if ch == "DBO":
                        data = compare(data,8,8,50,patern,ch)

                if ch == "CDBO":
                        data = compare(data,4,4,50,patern,ch)

                if ch == "SFR":
                        data = compare(data,1,0.512,10,patern,ch)

                if ch == "RSR":
                        data = compare(data,1,1,8,patern,ch)

                if ch == "UAR":
                        data = compare(data,2,2,250,patern,ch)

        return data



with open(sys.argv[1], "r") as json_file:
    data = json.load(json_file)

data = result(data,sys.argv[2])

with open(sys.argv[1], 'w') as f:
        json.dump(data, f)

