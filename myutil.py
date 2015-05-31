def sync_property(src, srcname, dst, dstname=None):
    if not dstname: dstname = srcname
    setattr(dst, dstname, getattr(src,srcname))
    def listener(ins, val):
        setattr(dst, dstname, val)
    src.bind(**{srcname:listener})
