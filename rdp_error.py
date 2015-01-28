import struct
#Everything was pulled from http://msdn.microsoft.com/en-us/library/cc240544.aspx



rdp_error_dict = dict()
# Error to Code
rdp_error_dict['ERRINFO_CB_SESSION_ONLINE_VM_NO_DNS']               = 0x0000407
rdp_error_dict['ERRINFO_SERVER_INSUFFICIENT_PRIVILEGES']            = 0x00000009
rdp_error_dict['ERRINFO_CB_SESSION_ONLINE_VM_BOOT_TIMEOUT']         = 0x0000411
rdp_error_dict['ERRINFO_INVALIDINPUTPDUMOUSE']                      = 0x000010D0
rdp_error_dict['ERRINFO_CB_SESSION_ONLINE_VM_SESSMON_FAILED']       = 0x0000412
rdp_error_dict['ERRINFO_CB_CONNECTION_CANCELLED']                   = 0x0000409
rdp_error_dict['ERRINFO_RPC_INITIATED_LOGOFF']                      = 0x00000002
rdp_error_dict['ERRINFO_LOGOFF_BY_USER']                            = 0x0000000C
rdp_error_dict['ERRINFO_UPDATESESSIONKEYFAILED']                    = 0x00001191
rdp_error_dict['ERRINFO_CREATEUSERDATAFAILED']                      = 0x000010D2
rdp_error_dict['ERRINFO_LICENSE_CANT_UPGRADE_LICENSE']              = 0x00000109
rdp_error_dict['ERRINFO_LICENSE_BAD_CLIENT_ENCRYPTION']             = 0x00000108
rdp_error_dict['ERRINFO_INVALIDREFRESHRECTPDU']                     = 0x000010D1
rdp_error_dict['ERRINFO_TIMEZONEKEYNAMELENGTHTOOLONG']              = 0x00001131
rdp_error_dict['ERRINFO_VCDATATOOLONG']                             = 0x0000112B
rdp_error_dict['ERRINFO_PERSISTENTKEYPDUTOOMANYCACHEKEYS']          = 0x000010DD
rdp_error_dict['ERRINFO_BADSUPRESSOUTPUTPDU']                       = 0x000010E3
rdp_error_dict['ERRINFO_LICENSE_NO_REMOTE_CONNECTIONS']             = 0x0000010A
rdp_error_dict['ERRINFO_GDIPLUSPDUBADLENGTH']                       = 0x000010F8
rdp_error_dict['ERRINFO_LOGON_TIMEOUT']                             = 0x00000004
rdp_error_dict['ERRINFO_CB_CONNECTION_ERROR_INVALID_SETTINGS']      = 0x0000410
rdp_error_dict['ERRINFO_VCDECODINGERROR']                           = 0x00001133
rdp_error_dict['ERRINFO_LICENSE_NO_LICENSE_SERVER']                 = 0x00000101
rdp_error_dict['ERRINFO_GRAPHICSMODENOTSUPPORTED']                  = 0x0000112D
rdp_error_dict['ERRINFO_RPC_INITIATED_DISCONNECT']                  = 0x00000001
rdp_error_dict['ERRINFO_BADMONITORDATA']                            = 0x00001129
rdp_error_dict['ERRINFO_OFFSCRCACHEERRORPDUBADLENGTH']              = 0x000010F6
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT17']                    = 0x00001120
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT16']                    = 0x0000111F
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT15']                    = 0x0000111E
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT14']                    = 0x0000111D
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT13']                    = 0x0000111C
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT12']                    = 0x0000111B
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT11']                    = 0x0000111A
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT10']                    = 0x00001119
rdp_error_dict['ERRINFO_LICENSE_BAD_CLIENT_MSG']                    = 0x00000103
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT19']                    = 0x00001122
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT18']                    = 0x00001121
rdp_error_dict['ERRINFO_VCHANNELSTOOMANY']                          = 0x000010F0
rdp_error_dict['ERRINFO_OUT_OF_MEMORY']                             = 0x00000006
rdp_error_dict['ERRINFO_VCDECOMPRESSEDREASSEMBLEFAILED']            = 0x0000112A
rdp_error_dict['ERRINFO_CONTROLPDUSEQUENCE']                        = 0x000010CD
rdp_error_dict['ERRINFO_INPUTPDUBADLENGTH']                         = 0x000010DE
rdp_error_dict['ERRINFO_VIRTUALCHANNELDECOMPRESSIONERR']            = 0x000010EC
rdp_error_dict['ERRINFO_ENCPKGMISMATCH']                            = 0x00001194
rdp_error_dict['ERRINFO_GRAPHICSSUBSYSTEMRESETFAILED']              = 0x0000112E
rdp_error_dict['ERRINFO_CB_DESTINATION_POOL_NOT_FREE']              = 0x0000408
rdp_error_dict['ERRINFO_BAD_FRAME_ACK_DATA']                        = 0x0000112C
rdp_error_dict['ERRINFO_LICENSE_HWID_DOESNT_MATCH_LICENSE']         = 0x00000104
rdp_error_dict['ERRINFO_UNKNOWNPDUTYPE']                            = 0x000010CA
rdp_error_dict['ERRINFO_PERSISTENTKEYPDUILLEGALFIRST']              = 0x000010DB
rdp_error_dict['ERRINFO_LICENSE_CLIENT_ENDED_PROTOCOL']             = 0x00000107
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT22']                    = 0x00001125
rdp_error_dict['ERRINFO_UNKNOWNPDUTYPE2']                           = 0x000010C9
rdp_error_dict['ERRINFO_PERSISTENTKEYPDUTOOMANYTOTALKEYS']          = 0x000010DC
rdp_error_dict['ERRINFO_INVALIDVCCOMPRESSIONTYPE']                  = 0x000010ED
rdp_error_dict['ERRINFO_LICENSE_BAD_CLIENT_LICENSE']                = 0x00000105
rdp_error_dict['ERRINFO_REMOTEAPPSNOTENABLED']                      = 0x000010F3
rdp_error_dict['ERRINFO_BITMAPCACHEERRORPDUBADLENGTH2']             = 0x000010F5
rdp_error_dict['ERRINFO_INVALIDCHANNELID']                          = 0x000010EF
rdp_error_dict['ERRINFO_LICENSE_INTERNAL']                          = 0x00000100
rdp_error_dict['ERRINFO_PERSISTENTKEYPDUBADLENGTH']                 = 0x000010DA
rdp_error_dict['ERRINFO_DECRYPTFAILED2']                            = 0x00001195
rdp_error_dict['ERRINFO_CB_LOADING_DESTINATION']                    = 0x0000402
rdp_error_dict['ERRINFO_INVALIDCONTROLPDUACTION']                   = 0x000010CE
rdp_error_dict['ERRINFO_CACHECAPNOTSET']                            = 0x000010F4
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT9']                     = 0x00001118
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT8']                     = 0x00001117
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT7']                     = 0x00001116
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT6']                     = 0x00001115
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT5']                     = 0x00001114
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT4']                     = 0x00001113
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT3']                     = 0x00001112
rdp_error_dict['ERRINFO_CB_DESTINATION_NOT_FOUND']                  = 0x0000400
rdp_error_dict['ERRINFO_CONFIRMACTIVEPDUTOOSHORT']                  = 0x000010E5
rdp_error_dict['ERRINFO_NOCURSORCACHE']                             = 0x000010E9
rdp_error_dict['ERRINFO_ENCRYPTFAILED']                             = 0x00001193
rdp_error_dict['ERRINFO_DATAPDUSEQUENCE']                           = 0x000010CB
rdp_error_dict['ERRINFO_BITMAPCACHEERRORPDUBADLENGTH']              = 0x000010DF
rdp_error_dict['ERRINFO_CONFIRMACTIVEWRONGORIGINATOR']              = 0x000010D5
rdp_error_dict['ERRINFO_CONFIRMACTIVEWRONGSHAREID']                 = 0x000010D4
rdp_error_dict['ERRINFO_CB_SESSION_ONLINE_VM_BOOT']                 = 0x0000406
rdp_error_dict['ERRINFO_RPC_INITIATED_DISCONNECT_BYUSER']           = 0x0000000B
rdp_error_dict['ERRINFO_LICENSE_NO_LICENSE']                        = 0x00000102
rdp_error_dict['ERRINFO_SHAREDATATOOSHORT']                         = 0x000010E2
rdp_error_dict['ERRINFO_BADCAPABILITIES']                           = 0x000010EA
rdp_error_dict['ERRINFO_CONNECTFAILED']                             = 0x000010D3
rdp_error_dict['ERRINFO_TIMEZONEKEYNAMELENGTHTOOSHORT']             = 0x00001130
rdp_error_dict['ERRINFO_VCHANNELDATATOOSHORT']                      = 0x000010E1
rdp_error_dict['ERRINFO_CB_REDIRECTING_TO_DESTINATION']             = 0x0000404
rdp_error_dict['ERRINFO_DISCONNECTED_BY_OTHERCONNECTION']           = 0x00000005
rdp_error_dict['ERRINFO_DYNAMICDSTDISABLEDFIELDMISSING']            = 0x00001132
rdp_error_dict['ERRINFO_GRAPHICSSUBSYSTEMFAILED']                   = 0x0000112F
rdp_error_dict['ERRINFO_DNGCACHEERRORPDUBADLENGTH']                 = 0x000010F7
rdp_error_dict['ERRINFO_LICENSE_CANT_FINISH_PROTOCOL']              = 0x00000106
rdp_error_dict['ERRINFO_INVALIDINPUTPDUTYPE']                       = 0x000010CF
rdp_error_dict['ERRINFO_DECRYPTFAILED']                             = 0x00001192
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT2']                     = 0x00001111
rdp_error_dict['ERRINFO_CAPABILITYSETTOOSMALL']                     = 0x000010E7
rdp_error_dict['ERRINFO_CAPABILITYSETTOOLARGE']                     = 0x000010E8
rdp_error_dict['ERRINFO_CB_SESSION_ONLINE_VM_WAKE']                 = 0x0000405
rdp_error_dict['ERRINFO_SERVER_DENIED_CONNECTION']                  = 0x00000007
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT23']                    = 0x00001126
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT20']                    = 0x00001123
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT21']                    = 0x00001124
rdp_error_dict['ERRINFO_IDLE_TIMEOUT']                              = 0x00000003
rdp_error_dict['ERRINFO_SECURITYDATATOOSHORT']                      = 0x000010E0
rdp_error_dict['ERRINFO_SERVER_FRESH_CREDENTIALS_REQUIRED']         = 0x0000000A



# Code to Error
rdp_error_dict[0x0000407]      = 'ERRINFO_CB_SESSION_ONLINE_VM_NO_DNS'
rdp_error_dict[0x00000009]     = 'ERRINFO_SERVER_INSUFFICIENT_PRIVILEGES'
rdp_error_dict[0x0000411]      = 'ERRINFO_CB_SESSION_ONLINE_VM_BOOT_TIMEOUT'
rdp_error_dict[0x000010D0]     = 'ERRINFO_INVALIDINPUTPDUMOUSE'
rdp_error_dict[0x0000412]      = 'ERRINFO_CB_SESSION_ONLINE_VM_SESSMON_FAILED'
rdp_error_dict[0x0000409]      = 'ERRINFO_CB_CONNECTION_CANCELLED'
rdp_error_dict[0x00000002]     = 'ERRINFO_RPC_INITIATED_LOGOFF'
rdp_error_dict[0x0000000C]     = 'ERRINFO_LOGOFF_BY_USER'
rdp_error_dict[0x00001191]     = 'ERRINFO_UPDATESESSIONKEYFAILED'
rdp_error_dict[0x000010D2]     = 'ERRINFO_CREATEUSERDATAFAILED'
rdp_error_dict[0x00000109]     = 'ERRINFO_LICENSE_CANT_UPGRADE_LICENSE'
rdp_error_dict[0x00000108]     = 'ERRINFO_LICENSE_BAD_CLIENT_ENCRYPTION'
rdp_error_dict[0x000010D1]     = 'ERRINFO_INVALIDREFRESHRECTPDU'
rdp_error_dict[0x00001131]     = 'ERRINFO_TIMEZONEKEYNAMELENGTHTOOLONG'
rdp_error_dict[0x0000112B]     = 'ERRINFO_VCDATATOOLONG'
rdp_error_dict[0x000010DD]     = 'ERRINFO_PERSISTENTKEYPDUTOOMANYCACHEKEYS'
rdp_error_dict[0x000010E3]     = 'ERRINFO_BADSUPRESSOUTPUTPDU'
rdp_error_dict[0x0000010A]     = 'ERRINFO_LICENSE_NO_REMOTE_CONNECTIONS'
rdp_error_dict[0x000010F8]     = 'ERRINFO_GDIPLUSPDUBADLENGTH'
rdp_error_dict[0x00000004]     = 'ERRINFO_LOGON_TIMEOUT'
rdp_error_dict[0x0000410]      = 'ERRINFO_CB_CONNECTION_ERROR_INVALID_SETTINGS'
rdp_error_dict[0x00001133]     = 'ERRINFO_VCDECODINGERROR'
rdp_error_dict[0x00000101]     = 'ERRINFO_LICENSE_NO_LICENSE_SERVER'
rdp_error_dict[0x0000112D]     = 'ERRINFO_GRAPHICSMODENOTSUPPORTED'
rdp_error_dict[0x00000001]     = 'ERRINFO_RPC_INITIATED_DISCONNECT'
rdp_error_dict[0x00001129]     = 'ERRINFO_BADMONITORDATA'
rdp_error_dict[0x000010F6]     = 'ERRINFO_OFFSCRCACHEERRORPDUBADLENGTH'
rdp_error_dict[0x00001120]     = 'ERRINFO_SECURITYDATATOOSHORT17'
rdp_error_dict[0x0000111F]     = 'ERRINFO_SECURITYDATATOOSHORT16'
rdp_error_dict[0x0000111E]     = 'ERRINFO_SECURITYDATATOOSHORT15'
rdp_error_dict[0x0000111D]     = 'ERRINFO_SECURITYDATATOOSHORT14'
rdp_error_dict[0x0000111C]     = 'ERRINFO_SECURITYDATATOOSHORT13'
rdp_error_dict[0x0000111B]     = 'ERRINFO_SECURITYDATATOOSHORT12'
rdp_error_dict[0x0000111A]     = 'ERRINFO_SECURITYDATATOOSHORT11'
rdp_error_dict[0x00001119]     = 'ERRINFO_SECURITYDATATOOSHORT10'
rdp_error_dict[0x00000103]     = 'ERRINFO_LICENSE_BAD_CLIENT_MSG'
rdp_error_dict[0x00001122]     = 'ERRINFO_SECURITYDATATOOSHORT19'
rdp_error_dict[0x00001121]     = 'ERRINFO_SECURITYDATATOOSHORT18'
rdp_error_dict[0x000010F0]     = 'ERRINFO_VCHANNELSTOOMANY'
rdp_error_dict[0x00000006]     = 'ERRINFO_OUT_OF_MEMORY'
rdp_error_dict[0x0000112A]     = 'ERRINFO_VCDECOMPRESSEDREASSEMBLEFAILED'
rdp_error_dict[0x000010CD]     = 'ERRINFO_CONTROLPDUSEQUENCE'
rdp_error_dict[0x000010DE]     = 'ERRINFO_INPUTPDUBADLENGTH'
rdp_error_dict[0x000010EC]     = 'ERRINFO_VIRTUALCHANNELDECOMPRESSIONERR'
rdp_error_dict[0x00001194]     = 'ERRINFO_ENCPKGMISMATCH'
rdp_error_dict[0x0000112E]     = 'ERRINFO_GRAPHICSSUBSYSTEMRESETFAILED'
rdp_error_dict[0x0000408]      = 'ERRINFO_CB_DESTINATION_POOL_NOT_FREE'
rdp_error_dict[0x0000112C]     = 'ERRINFO_BAD_FRAME_ACK_DATA'
rdp_error_dict[0x00000104]     = 'ERRINFO_LICENSE_HWID_DOESNT_MATCH_LICENSE'
rdp_error_dict[0x000010CA]     = 'ERRINFO_UNKNOWNPDUTYPE'
rdp_error_dict[0x000010DB]     = 'ERRINFO_PERSISTENTKEYPDUILLEGALFIRST'
rdp_error_dict[0x00000107]     = 'ERRINFO_LICENSE_CLIENT_ENDED_PROTOCOL'
rdp_error_dict[0x00001125]     = 'ERRINFO_SECURITYDATATOOSHORT22'
rdp_error_dict[0x000010C9]     = 'ERRINFO_UNKNOWNPDUTYPE2'
rdp_error_dict[0x000010DC]     = 'ERRINFO_PERSISTENTKEYPDUTOOMANYTOTALKEYS'
rdp_error_dict[0x000010ED]     = 'ERRINFO_INVALIDVCCOMPRESSIONTYPE'
rdp_error_dict[0x00000105]     = 'ERRINFO_LICENSE_BAD_CLIENT_LICENSE'
rdp_error_dict[0x000010F3]     = 'ERRINFO_REMOTEAPPSNOTENABLED'
rdp_error_dict[0x000010F5]     = 'ERRINFO_BITMAPCACHEERRORPDUBADLENGTH2'
rdp_error_dict[0x000010EF]     = 'ERRINFO_INVALIDCHANNELID'
rdp_error_dict[0x00000100]     = 'ERRINFO_LICENSE_INTERNAL'
rdp_error_dict[0x000010DA]     = 'ERRINFO_PERSISTENTKEYPDUBADLENGTH'
rdp_error_dict[0x00001195]     = 'ERRINFO_DECRYPTFAILED2'
rdp_error_dict[0x0000402]      = 'ERRINFO_CB_LOADING_DESTINATION'
rdp_error_dict[0x000010CE]     = 'ERRINFO_INVALIDCONTROLPDUACTION'
rdp_error_dict[0x000010F4]     = 'ERRINFO_CACHECAPNOTSET'
rdp_error_dict[0x00001118]     = 'ERRINFO_SECURITYDATATOOSHORT9'
rdp_error_dict[0x00001117]     = 'ERRINFO_SECURITYDATATOOSHORT8'
rdp_error_dict[0x00001116]     = 'ERRINFO_SECURITYDATATOOSHORT7'
rdp_error_dict[0x00001115]     = 'ERRINFO_SECURITYDATATOOSHORT6'
rdp_error_dict[0x00001114]     = 'ERRINFO_SECURITYDATATOOSHORT5'
rdp_error_dict[0x00001113]     = 'ERRINFO_SECURITYDATATOOSHORT4'
rdp_error_dict[0x00001112]     = 'ERRINFO_SECURITYDATATOOSHORT3'
rdp_error_dict[0x0000400]      = 'ERRINFO_CB_DESTINATION_NOT_FOUND'
rdp_error_dict[0x000010E5]     = 'ERRINFO_CONFIRMACTIVEPDUTOOSHORT'
rdp_error_dict[0x000010E9]     = 'ERRINFO_NOCURSORCACHE'
rdp_error_dict[0x00001193]     = 'ERRINFO_ENCRYPTFAILED'
rdp_error_dict[0x000010CB]     = 'ERRINFO_DATAPDUSEQUENCE'
rdp_error_dict[0x000010DF]     = 'ERRINFO_BITMAPCACHEERRORPDUBADLENGTH'
rdp_error_dict[0x000010D5]     = 'ERRINFO_CONFIRMACTIVEWRONGORIGINATOR'
rdp_error_dict[0x000010D4]     = 'ERRINFO_CONFIRMACTIVEWRONGSHAREID'
rdp_error_dict[0x0000406]      = 'ERRINFO_CB_SESSION_ONLINE_VM_BOOT'
rdp_error_dict[0x0000000B]     = 'ERRINFO_RPC_INITIATED_DISCONNECT_BYUSER'
rdp_error_dict[0x00000102]     = 'ERRINFO_LICENSE_NO_LICENSE'
rdp_error_dict[0x000010E2]     = 'ERRINFO_SHAREDATATOOSHORT'
rdp_error_dict[0x000010EA]     = 'ERRINFO_BADCAPABILITIES'
rdp_error_dict[0x000010D3]     = 'ERRINFO_CONNECTFAILED'
rdp_error_dict[0x00001130]     = 'ERRINFO_TIMEZONEKEYNAMELENGTHTOOSHORT'
rdp_error_dict[0x000010E1]     = 'ERRINFO_VCHANNELDATATOOSHORT'
rdp_error_dict[0x0000404]      = 'ERRINFO_CB_REDIRECTING_TO_DESTINATION'
rdp_error_dict[0x00000005]     = 'ERRINFO_DISCONNECTED_BY_OTHERCONNECTION'
rdp_error_dict[0x00001132]     = 'ERRINFO_DYNAMICDSTDISABLEDFIELDMISSING'
rdp_error_dict[0x0000112F]     = 'ERRINFO_GRAPHICSSUBSYSTEMFAILED'
rdp_error_dict[0x000010F7]     = 'ERRINFO_DNGCACHEERRORPDUBADLENGTH'
rdp_error_dict[0x00000106]     = 'ERRINFO_LICENSE_CANT_FINISH_PROTOCOL'
rdp_error_dict[0x000010CF]     = 'ERRINFO_INVALIDINPUTPDUTYPE'
rdp_error_dict[0x00001192]     = 'ERRINFO_DECRYPTFAILED'
rdp_error_dict[0x00001111]     = 'ERRINFO_SECURITYDATATOOSHORT2'
rdp_error_dict[0x000010E7]     = 'ERRINFO_CAPABILITYSETTOOSMALL'
rdp_error_dict[0x000010E8]     = 'ERRINFO_CAPABILITYSETTOOLARGE'
rdp_error_dict[0x0000405]      = 'ERRINFO_CB_SESSION_ONLINE_VM_WAKE'
rdp_error_dict[0x00000007]     = 'ERRINFO_SERVER_DENIED_CONNECTION'
rdp_error_dict[0x00001126]     = 'ERRINFO_SECURITYDATATOOSHORT23'
rdp_error_dict[0x00001123]     = 'ERRINFO_SECURITYDATATOOSHORT20'
rdp_error_dict[0x00001124]     = 'ERRINFO_SECURITYDATATOOSHORT21'
rdp_error_dict[0x00000003]     = 'ERRINFO_IDLE_TIMEOUT'
rdp_error_dict[0x000010E0]     = 'ERRINFO_SECURITYDATATOOSHORT'
rdp_error_dict[0x0000000A]     = 'ERRINFO_SERVER_FRESH_CREDENTIALS_REQUIRED'



# Error Description
rdp_err_description_dict = dict()
rdp_err_description_dict[0x0000407]      = 'The IP address of the target endpoint cannot be determined.'
rdp_err_description_dict[0x00000009]     = 'The user cannot connect to the server due to insufficient access privileges.'
rdp_err_description_dict[0x0000411]      = 'A time-out occurred while the target endpoint was being started.'
rdp_err_description_dict[0x000010D0]     = 'A Slow-Path Mouse Event or Extended Mouse Event has been received with an invalid pointerFlags field.\nA Fast-Path Mouse Event or Fast-Path Extended Mouse Event has been received with an invalid pointerFlags field.'
rdp_err_description_dict[0x0000412]      = 'A session monitoring error occurred while the target endpoint was being started.'
rdp_err_description_dict[0x0000409]      = 'Processing of the connection has been cancelled.'
rdp_err_description_dict[0x00000002]     = 'The disconnection was due to a forced logoff initiated by an administrative tool on the server in another session.'
rdp_err_description_dict[0x0000000C]     = 'The disconnection was initiated by the user logging off his or her session on the server.'
rdp_err_description_dict[0x00001191]     = 'An attempt to update the session keys while using Standard RDP Security mechanisms failed.'
rdp_err_description_dict[0x000010D2]     = 'The server failed to construct the GCC Conference Create Response user data.'
rdp_err_description_dict[0x00000109]     = 'The Client Access License stored by the client could not be upgraded or renewed.'
rdp_err_description_dict[0x00000108]     = 'A licensing message was incorrectly encrypted.'
rdp_err_description_dict[0x000010D1]     = 'An invalid Refresh Rect PDU has been received.'
rdp_err_description_dict[0x00001131]     = 'The length reported in the cbDynamicDSTTimeZoneKeyName field of the Extended Info Packet is too long.'
rdp_err_description_dict[0x0000112B]     = 'The size of a received Virtual Channel PDU exceeds the chunking size specified in the Virtual Channel Capability Set.'
rdp_err_description_dict[0x000010DD]     = 'A Persistent Key List PDU was received which specified an invalid total number of keys for a bitmap cache that is sent from client to server).'
rdp_err_description_dict[0x000010E3]     = 'There is not enough data to process Suppress Output PDU Data.\nThe allowDisplayUpdates field of the Suppress Output PDU Data is invalid.'
rdp_err_description_dict[0x0000010A]     = 'The remote computer is not licensed to accept remote connections.'
rdp_err_description_dict[0x000010F8]     = 'There is not enough data to process a GDI+ Error PDU.'
rdp_err_description_dict[0x00000004]     = 'The active session limit timer on the server has elapsed.'
rdp_err_description_dict[0x0000410]      = 'The settings contained in the routingToken field of the X.224 Connection Request PDU cannot be validated.'
rdp_err_description_dict[0x00001133]     = 'An error occurred when processing dynamic virtual channel data.'
rdp_err_description_dict[0x00000101]     = 'A Remote Desktop License Server could not be found to provide a license.'
rdp_err_description_dict[0x0000112D]     = 'The graphics mode requested by the client is not supported by the server.'
rdp_err_description_dict[0x00000001]     = 'The disconnection was initiated by an administrative tool on the server in another session.'
rdp_err_description_dict[0x00001129]     = 'The monitorCount field in the Client Monitor Data is invalid.'
rdp_err_description_dict[0x000010F6]     = 'There is not enough data to process an Offscreen Bitmap Cache Error PDU.'
rdp_err_description_dict[0x00001120]     = 'There is not enough data to read the clientAddressFamily and cbClientAddress fields in the Extended Info Packet.'
rdp_err_description_dict[0x0000111F]     = 'The cbAutoReconnectCookie field in the Extended Info Packet contains a value which is larger than the maximum allowed length of 128 bytes.'
rdp_err_description_dict[0x0000111E]     = 'There is not enough data to read the autoReconnectCookie field in the Extended Info Packet.'
rdp_err_description_dict[0x0000111D]     = 'There is not enough data to read the cbAutoReconnectCookie field in the Extended Info Packet.'
rdp_err_description_dict[0x0000111C]     = 'There is not enough data to read the performanceFlags field in the Extended Info Packet.'
rdp_err_description_dict[0x0000111B]     = 'There is not enough data to read the clientSessionId field in the Extended Info Packet.'
rdp_err_description_dict[0x0000111A]     = 'There is not enough data to read the clientTimeZone field in the Extended Info Packet.'
rdp_err_description_dict[0x00001119]     = 'There is not enough data to read the clientDir field in the Extended Info Packet.'
rdp_err_description_dict[0x00000103]     = 'The remote computer received an invalid licensing message from the client.'
rdp_err_description_dict[0x00001122]     = 'There is not enough data to read the cbClientDir field in the Extended Info Packet.'
rdp_err_description_dict[0x00001121]     = 'There is not enough data to read the clientAddress field in the Extended Info Packet.'
rdp_err_description_dict[0x000010F0]     = 'The client requested more than the maximum allowed 31 static virtual channels in the Client Network Data.'
rdp_err_description_dict[0x00000006]     = 'The server ran out of available memory resources.'
rdp_err_description_dict[0x0000112A]     = 'The server-side decompression buffer is invalid, or the size of the decompressed VC data exceeds the chunking size specified in the Virtual Channel Capability Set.'
rdp_err_description_dict[0x000010CD]     = 'An out-of-sequence Slow-Path Non-Data PDU has been received.'
rdp_err_description_dict[0x000010DE]     = 'There is not enough data to process Input Event PDU Data or a Fast-Path Input Event PDU.'
rdp_err_description_dict[0x000010EC]     = 'An error occurred while using the bulk compressor to decompress a Virtual Channel PDU'
rdp_err_description_dict[0x00001194]     = 'Failed to find a usable Encryption Method in the encryptionMethods field of the Client Security Data.'
rdp_err_description_dict[0x0000112E]     = 'The server-side graphics subsystem failed to reset.'
rdp_err_description_dict[0x0000408]      = 'There are no available endpoints in the pool managed by the Connection Broker.'
rdp_err_description_dict[0x0000112C]     = 'There is not enough data to read a TS_FRAME_ACKNOWLEDGE_PDU.'
rdp_err_description_dict[0x00000104]     = 'The Client Access License stored by the client has been modified.'
rdp_err_description_dict[0x000010CA]     = 'Unknown pduType field in a received Share Control Header.'
rdp_err_description_dict[0x000010DB]     = 'A Persistent Key List PDU marked as PERSIST_PDU_FIRST was received after the reception of a prior Persistent Key List PDU also marked as PERSIST_PDU_FIRST.'
rdp_err_description_dict[0x00000107]     = 'The client prematurely ended the licensing protocol.'
rdp_err_description_dict[0x00001125]     = 'There is not enough data to read the clientSessionId field in the Extended Info Packet.'
rdp_err_description_dict[0x000010C9]     = 'Unknown pduType2 field in a received Share Data Header.'
rdp_err_description_dict[0x000010DC]     = 'A Persistent Key List PDU was received which specified a total number of bitmap cache entries larger than 262144.'
rdp_err_description_dict[0x000010ED]     = 'An invalid bulk compression package was specified in the flags field of the Channel PDU Header.'
rdp_err_description_dict[0x00000105]     = 'The Client Access License stored by the client is in an invalid format'
rdp_err_description_dict[0x000010F3]     = 'The INFO_RAIL flag MUST be set in the flags field of the Info Packet as the session on the remote server can only host remote applications.'
rdp_err_description_dict[0x000010F5]     = 'The NumInfoBlocks field in the Bitmap Cache Error PDU Data is inconsistent with the amount of data in the Info field.'
rdp_err_description_dict[0x000010EF]     = 'An invalid MCS channel ID was specified in the mcsPdu field of the Virtual Channel PDU.'
rdp_err_description_dict[0x00000100]     = 'An internal error has occurred in the Terminal Services licensing component.'
rdp_err_description_dict[0x000010DA]     = 'There is not enough data to process a Persistent Key List PDU.'
rdp_err_description_dict[0x00001195]     = 'Unencrypted data was encountered in a protocol stream which is meant to be encrypted with Standard RDP Security mechanisms.'
rdp_err_description_dict[0x0000402]      = 'The target endpoint to which the client is being redirected is disconnecting from the Connection Broker.'
rdp_err_description_dict[0x000010CE]     = 'A Control PDU has been received with an invalid action field.'
rdp_err_description_dict[0x000010F4]     = 'The client sent a Persistent Key List PDU without including the prerequisite Revision 2 Bitmap Cache Capability Set in the Confirm Active PDU.'
rdp_err_description_dict[0x00001118]     = 'There is not enough data to read the cbClientDir field in the Extended Info Packet.'
rdp_err_description_dict[0x00001117]     = 'There is not enough data to read the clientAddress field in the Extended Info Packet.'
rdp_err_description_dict[0x00001116]     = 'There is not enough data to read the clientAddressFamily and cbClientAddress fields in the Extended Info Packet.'
rdp_err_description_dict[0x00001115]     = 'There is not enough data to read the CodePage, flags, cbDomain, cbUserName, cbPassword, cbAlternateShell, and cbWorkingDir fields in the Info Packet.'
rdp_err_description_dict[0x00001114]     = 'There is not enough data to read the CodePage, flags, cbDomain, cbUserName, cbPassword, cbAlternateShell, cbWorkingDir, Domain, UserName, Password, AlternateShell, and WorkingDir fields in the Info Packet.'
rdp_err_description_dict[0x00001113]     = 'There is not enough data to read the basicSecurityHeader and length fields of the Security Exchange PDU Data.'
rdp_err_description_dict[0x00001112]     = 'There is not enough data to read a Non-FIPS Security Header or FIPS Security Header.'
rdp_err_description_dict[0x0000400]      = 'The target endpoint could not be found.'
rdp_err_description_dict[0x000010E5]     = 'There is not enough data to read the shareControlHeader, shareId, originatorId, lengthSourceDescriptor, and lengthCombinedCapabilities fields of the Confirm Active PDU Data.\nThere is not enough data to read the sourceDescriptor, numberCapabilities, pad2Octets, and capabilitySets fields of the Confirm Active PDU Data.'
rdp_err_description_dict[0x000010E9]     = 'Both the colorPointerCacheSize and pointerCacheSize fields in the Pointer Capability Set are set to zero.\nThe pointerCacheSize field in the Pointer Capability Set is not present, and the colorPointerCacheSize field is set to zero.'
rdp_err_description_dict[0x00001193]     = 'Encryption using Standard RDP Security mechanisms failed.'
rdp_err_description_dict[0x000010CB]     = 'An out-of-sequence Slow-Path Data PDU has been received.'
rdp_err_description_dict[0x000010DF]     = 'There is not enough data to process the shareDataHeader, NumInfoBlocks, Pad1, and Pad2 fields of the Bitmap Cache Error PDU Data.'
rdp_err_description_dict[0x000010D5]     = 'A Confirm Active PDU was received from the client with an invalid originatorId field.'
rdp_err_description_dict[0x000010D4]     = 'A Confirm Active PDU was received from the client with an invalid shareId field.'
rdp_err_description_dict[0x0000406]      = 'An error occurred while the target endpoint was being started.'
rdp_err_description_dict[0x0000000B]     = "The disconnection was initiated by an administrative tool on the server running in the user's session."
rdp_err_description_dict[0x00000102]     = 'There are no Client Access Licenses available for the target remote computer.'
rdp_err_description_dict[0x000010E2]     = 'There is not enough data to process Control PDU Data.\nThere is not enough data to read a complete Share Control Header.\nThere is not enough data to read a complete Share Data Header of a Slow-Path Data PDU.\nThere is not enough data to process Font List PDU Data.'
rdp_err_description_dict[0x000010EA]     = 'The capabilities received from the client in the Confirm Active PDU were not accepted by the server.'
rdp_err_description_dict[0x000010D3]     = 'Processing during the Channel Connection phase of the RDP Connection Sequence has failed.'
rdp_err_description_dict[0x00001130]     = 'There is not enough data to read the cbDynamicDSTTimeZoneKeyName field in the Extended Info Packet.'
rdp_err_description_dict[0x000010E1]     = 'There is not enough data in the Client Network Data to read the virtual channel configuration data.\nThere is not enough data to read a complete Channel PDU Header.'
rdp_err_description_dict[0x0000404]      = 'An error occurred while the connection was being redirected to the target endpoint.'
rdp_err_description_dict[0x00000005]     = 'Another user connected to the server, forcing the disconnection of the current connection.'
rdp_err_description_dict[0x00001132]     = 'The dynamicDaylightTimeDisabled field is not present in the Extended Info Packet.'
rdp_err_description_dict[0x0000112F]     = 'The server-side graphics subsystem is in an error state and unable to continue graphics encoding.'
rdp_err_description_dict[0x000010F7]     = 'There is not enough data to process a DrawNineGrid Cache Error PDU.'
rdp_err_description_dict[0x00000106]     = 'Network problems have caused the licensing protocol to be terminated.'
rdp_err_description_dict[0x000010CF]     = 'A Slow-Path Input Event has been received with an invalid messageType field.\nA Fast-Path Input Event has been received with an invalid eventCode field.'
rdp_err_description_dict[0x00001192]     = 'Decryption using Standard RDP Security mechanisms failed.\nSession key creation using Standard RDP Security mechanisms failed.'
rdp_err_description_dict[0x00001111]     = 'There is not enough data to read a Basic Security Header.'
rdp_err_description_dict[0x000010E7]     = 'There is not enough data to read the capabilitySetType and the lengthCapability fields in a received Capability Set.'
rdp_err_description_dict[0x000010E8]     = 'A Capability Set has been received with a lengthCapability field that contains a value greater than the total length of the data received.'
rdp_err_description_dict[0x0000405]      = 'An error occurred while the target endpoint was being awakened.'
rdp_err_description_dict[0x00000007]     = 'The server denied the connection.'
rdp_err_description_dict[0x00001126]     = 'There is not enough data to read the Client Info PDU Data.'
rdp_err_description_dict[0x00001123]     = 'There is not enough data to read the clientDir field in the Extended Info Packet.'
rdp_err_description_dict[0x00001124]     = 'There is not enough data to read the clientTimeZone field in the Extended Info Packet.'
rdp_err_description_dict[0x00000003]     = 'The idle session limit timer on the server has elapsed.'
rdp_err_description_dict[0x000010E0]     = 'The dataSignature field of the Fast-Path Input Event PDU does not contain enough data.\nThe fipsInformation and dataSignature fields of the Fast-Path Input Event PDU do not contain enough data.'
rdp_err_description_dict[0x0000000A]     = 'The server does not accept saved user credentials and requires that the user enter their credentials for each connection.'




class RDPError(Exception):
    
    def __init__(self, err_code, err_name, err_desc):
        self.err_code = err_code
        self.err_name = err_name
        self.err_desc = err_desc
        

def check_error(packet, padding = 0):
    if len(packet) > 1 and len(packet) >= 18:
        sharecontrolheader          = packet[:6]
        sharecontrolheader_len      = struct.unpack('h', sharecontrolheader[:2])[0]
        sharecontrolheader_type     = sharecontrolheader[2:4]
        type                        = struct.unpack('h', sharecontrolheader_type)[0] & 15
        pdu_id                      = struct.unpack('h', sharecontrolheader_type)[0] & 65520
        sharecontrolheader_source   = sharecontrolheader[4:6]
        shareID                     = packet[6:10]
        pad1                        = packet[10:11]
        streamID                    = packet[11:12]
        uncompressed_length         = packet[12:14]
        pdu_type_2                  = struct.unpack('b', packet[14:15])[0]
        compressedType              = struct.unpack('b', packet[15:16])[0]
        compressedLength            = packet[16:18]
        if pdu_type_2 == 47 and type == 7:
            error_info              = struct.unpack('<l', packet[18:22])[0]
            if rdp_error_dict.has_key(error_info):
                print '\n\n-------------Description of Error-------------\nNumber: %s       Name: %s\n\n%s\n----------------------------------------------' % (hex(error_info), rdp_error_dict[error_info],rdp_err_description_dict[error_info])
                raise RDPError(hex(error_info), rdp_error_dict[error_info],rdp_err_description_dict[error_info])
            else:
                print 'This is an error packet but no info found found in as to what it means. \nCheck to see if http://msdn.microsoft.com/en-us/library/cc240544.aspx has been updated.'
                raise RDPError(hex(error_info), rdp_error_dict[error_info],rdp_err_description_dict[error_info])