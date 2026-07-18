import json
import os


def recover_answers():
    brain_dir = "/home/saito/.gemini/antigravity-cli/brain/"
    subagent_ids = [
        "3fecb246-bc3c-4d4b-8c34-512f68bfcf6c",
        "bf7cf708-b999-410b-bc69-627265d822f2",
        "f528d067-3665-4b0f-8731-0a3e64b4a2f2",
        "fa219ca6-2cde-4324-8e33-322485eba8ed",
        "bbd7073d-4a8b-4ab9-887b-34f3413987f2",
        "32ea3c87-a8ed-4e43-83b4-c3db54525fcc",
        "fd7fdc7d-185b-4324-943c-1888d81de273",
        "83513378-4481-45aa-87cd-54c36c456e00",
        "6b5ca40b-0f25-463a-9f48-8e792b04b8bf",
        "6a84de35-65f3-4279-a50c-6cc6e6119418",
        "a26e3cbf-7942-4c30-b731-28da46b53ca0",
        "1a70021d-b860-4cba-adc2-0090b105f750",
        "1c5b268f-9f2a-4976-894c-1a2a77f9686f",
        "38c4c1d4-2485-490f-a79a-2d13e63a8643",
        "f47cade7-2ce5-40e6-ab85-bb35f2f30f7e",
        "78c270db-d63e-401f-808b-dd60090cd038",
        "5a1cfab3-9de6-42b7-b775-6c650a824e79",
        "bcdd9933-fd98-4f36-b0cd-44066159341c",
        "512eff77-41eb-48c8-a5ce-a3e5ca57ef87",
        "ae6d53e2-508b-4425-8cf9-242be3085db4",
        "93dc2399-d0a1-4b89-a4d7-c8b2721bfd3f",
        "bb2d0a3b-5e2a-4337-ac4d-4323c88b8ab2",
        "7b1bd6b5-bfa8-4d69-a34c-88b648800077",
        "a3c69e4b-a1f3-485d-be1b-f99990fb7150",
        "e1d4be36-fdb2-465d-9a19-2ca5de93b8a5",
        "fbeede89-e910-4388-b7ab-c324dca47f8c",
        "05bb34a4-253b-4517-ad2f-b0548a8d673f",
    ]

    recovered = []

    for sid in subagent_ids:
        transcript_path = os.path.join(
            brain_dir, sid, ".system_generated", "logs", "transcript_full.jsonl"
        )
        if not os.path.exists(transcript_path):
            continue

        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                try:
                    data = json.loads(line)
                    if "tool_calls" in data:
                        for call in data["tool_calls"]:
                            if call.get("name") == "write_to_file":
                                args = call.get("args", {})
                                code_content = args.get("CodeContent", "")
                                # code_content might be a JSON string representing the answers array
                                # Try parsing it
                                if code_content.strip().startswith("["):
                                    try:
                                        chunk_data = json.loads(code_content)
                                        if (
                                            isinstance(chunk_data, list)
                                            and len(chunk_data) > 0
                                            and "answer" in chunk_data[0]
                                        ):
                                            recovered.extend(chunk_data)
                                    except Exception:
                                        pass
                except:
                    pass

    with open("recovered_answers.json", "w", encoding="utf-8") as f:
        json.dump(recovered, f, ensure_ascii=False, indent=4)

    print(f"Recovered {len(recovered)} answers!")


if __name__ == "__main__":
    recover_answers()
