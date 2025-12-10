import json
from dataclasses import asdict
from utils.general import tlogger
from bom.generated.mpp import Mpp
from entrypoint import Bre01Flow

#update filename to absolute path of the testing packet
INPUT_FILE_NAME = "D:/projects/business_rule_engine/repos/bre01/test/packets/input.txt"

def main() :
    tlogger().info("-------------TESTING STARTED-------------")
    try:
        input_string = read_file(INPUT_FILE_NAME)
        payload = json.loads(input_string)
        tlogger().info("LOADED INPUT")
        mpp = Mpp.from_dict(payload) # PARSING INPUT JSON TO MPP OBJECT
        tlogger().info("PARSING DONE")
        result = Bre01Flow().execute(mpp) # CALLING THE BRE01 ENTRYPOINT FLOW
        tlogger().info(asdict(mpp))
        tlogger().info("-------------TESTING ENDED-------------")

    except Exception as e:
        tlogger().info(e)


def read_file(filename) :
    with open(filename, 'r') as file:
        data = file.read()
    return data

if __name__ == "__main__":
    main()
