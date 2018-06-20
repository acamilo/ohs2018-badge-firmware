#include "py/nlr.h"
#include "py/obj.h"
#include "py/runtime.h"
#include "py/binary.h"

STATIC const mp_map_elem_t badge_globals_table[] = {
    { MP_OBJ_NEW_QSTR(MP_QSTR___name__), MP_OBJ_NEW_QSTR(MP_QSTR_badge) },
};

STATIC MP_DEFINE_CONST_DICT (
    mp_module_badge_globals,
    badge_globals_table
);

const mp_obj_module_t mp_module_badge = {
    .base = { &mp_type_module },
    .globals = (mp_obj_dict_t*)&mp_module_badge_globals,
};
