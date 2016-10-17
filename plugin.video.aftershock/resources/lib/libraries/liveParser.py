# -*- coding: utf-8 -*-
#
# This Program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import os
import control, json, cleantitle


class LiveParser(object):
    filePath = ''
    basePath = control.dataPath

    def __init__(self, fileName, addon):
        self.filePath = os.path.join(self.basePath, fileName)
        return

    def parseFile(self):
        try :
            filename = open(self.filePath)
            result = filename.read()
            filename.close()
            channels = json.loads(result)

            channelNames = channels.keys()
            channelNames.sort()

            liveList = []
            for channel in channelNames:
                channelObj = channels[channel]
                try : enabled = channelObj['enabled']
                except : enabled = 'true'
                try : quality = channelObj['quality']
                except : quality = 'HD'
                if not enabled == 'false':
                    channelName = cleantitle.live(channel).title()
                    try :
                        if channelObj['direct'] == 'true': channelObj['direct'] = True
                        else : channelObj['direct'] = False
                    except:
                        channelObj['direct'] = True

                    liveList.append({'name':channelName, 'poster':channelObj['icon'],'url':channelObj['url'],'provider':channelObj['provider'],'source':channelObj['provider'],'direct':channelObj['direct'], 'quality':quality})
            return liveList
        except:
            pass