# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

import xbmc

from tools import (
    get_current_list_item_path,
    get_current_list_item_action_args,
    action_replace,
    update_query_params
)

if __name__ == "__main__":
    path = get_current_list_item_path()
    path = action_replace(path, {"smartPlay": "getSources"})
    path = update_query_params(path, {"hs_reload": "true"})

    action_args = get_current_list_item_action_args()
    xbmc.log(
        "context.hs: Source Select ({})".format(action_args['info']['title']),
        xbmc.LOGDEBUG,
    )
    xbmc.executebuiltin("PlayMedia({})".format(path))
