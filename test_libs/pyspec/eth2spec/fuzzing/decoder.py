from eth2spec.utils.ssz import ssz_typing as spec_ssz
import ssz


def translate_typ(typ) -> ssz.BaseSedes:
    """
    Translates a spec type to a Py-SSZ type description (sedes).
    :param typ: The spec type, a class.
    :return: The Py-SSZ equivalent.
    """
    if issubclass(typ, spec_ssz.Container):
        fields = typ.fields()
        return ssz.Container(
            [translate_typ(field_typ) for field_name, field_typ in zip(fields.keys, fields.types)])
    elif issubclass(typ, spec_ssz.ByteVector):
        return ssz.ByteVector(typ.type_byte_length())
    elif issubclass(typ, spec_ssz.Vector):
        return ssz.Vector(translate_typ(typ.element_cls()), typ.vector_length())
    elif issubclass(typ, spec_ssz.List):
        return ssz.List(translate_typ(typ.element_cls()), typ.limit())
    elif issubclass(typ, spec_ssz.Bitlist):
        return ssz.Bitlist(typ.limit())
    elif issubclass(typ, spec_ssz.Bitvector):
        return ssz.Bitvector(typ.vector_length())
    elif issubclass(typ, spec_ssz.boolean):
        return ssz.boolean
    elif issubclass(typ, spec_ssz.uint):
        byte_len = typ.type_byte_length()
        if byte_len == 1:
            return ssz.uint8
        elif byte_len == 2:
            return ssz.uint16
        elif byte_len == 4:
            return ssz.uint32
        elif byte_len == 8:
            return ssz.uint64
        elif byte_len == 16:
            return ssz.uint128
        elif byte_len == 32:
            return ssz.uint256
        else:
            raise TypeError("invalid uint size")
    else:
        raise TypeError("Type not supported: {}".format(typ))


def translate_value(value, typ):
    """
    Translate a value output from Py-SSZ deserialization into the given spec type.
    :param value: The PySSZ value
    :param typ: The type from the spec to translate into
    :return: the translated value
    """
    if issubclass(typ, spec_ssz.uint):
        byte_len = typ.type_byte_length()
        if byte_len == 1:
            return spec_ssz.uint8(value)
        elif byte_len == 2:
            return spec_ssz.uint16(value)
        elif byte_len == 4:
            return spec_ssz.uint32(value)
        elif byte_len == 8:
            return spec_ssz.uint64(value)
        elif byte_len == 16:
            return spec_ssz.uint128(value)
        elif byte_len == 32:
            return spec_ssz.uint256(value)
        else:
            raise TypeError("invalid uint size")
    elif issubclass(typ, (spec_ssz.List, spec_ssz.Vector)):
        return typ(*(translate_value(elem, typ.element_cls()) for elem in value))
    elif issubclass(typ, spec_ssz.boolean):
        return typ(value)
    elif issubclass(typ, (spec_ssz.Bitlist, spec_ssz.Bitvector)):
        return typ(value)  # TODO: may have changed, needs testing
    elif issubclass(typ, spec_ssz.ByteVector):
        return typ(value)
    if issubclass(typ, spec_ssz.Container):
        fields = typ.fields()
        return typ(**{f_name: translate_value(f_val, f_typ) for (f_val, (f_name, f_typ))
                      in zip(value, fields.keys, fields.types)})
    else:
        raise TypeError("Type not supported: {}".format(typ))
