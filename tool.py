#argv=sys.argv (input taken straight from the command line)
def main(argv):
    if not (4<=len(argv)<=5)
        usage()
        return BAD_ARGS
    dbname, verb, key, value=(argv[0:]+[None])[:4]
    if verb not in ['get','set','delete']:
        usage()
        return BAD_VERB
    db=db.connect(dbname)#Connect is another function which is to be defined
    try:
        if (verb=='get'):
            sys.stdout.write(db[key])
        if (verb=='set'):
            db[key]=value
            db.commit()
        else:
            del db[key]
            db.commit()
    except KeyError:
        sys.stderr.write("Key not found")
        return BAD_KEY
    return OK
