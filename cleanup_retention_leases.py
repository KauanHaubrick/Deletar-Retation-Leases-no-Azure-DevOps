import requests
import base64

AZURE_DEVOPS_PAT = "SEU_PAT_AQUI"
ORG = "SeuOrg"
PROJECT = "SeuProjeto"
PIPELINE_ID = 00

BASE_URL = f"https://dev.azure.com/{ORG}/{PROJECT}"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Basic {base64.b64encode(f':{AZURE_DEVOPS_PAT}'.encode()).decode()}"
}

def get_leases_for_pipeline():
    url = (
        f"{BASE_URL}/_apis/build/retention/leases"
        f"?definitionId={PIPELINE_ID}"
        f"&api-version=7.1-preview.1"
    )
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get("value", [])

def delete_leases():
    leases = get_leases_for_pipeline()
    print(f"Leases encontrados para a pipeline {PIPELINE_ID}: {len(leases)}")

    if not leases:
        print("Nenhum lease para remover.")
        return

    confirm = input("Deseja remover esses leases? (yes/no): ").lower()
    if confirm != "yes":
        print("Operação cancelada.")
        return

    for lease in leases:
        lease_id = lease["leaseId"]
        delete_url = (
            f"{BASE_URL}/_apis/build/retention/leases"
            f"?ids={lease_id}"
            f"&api-version=7.1-preview.1"
        )

        response = requests.delete(delete_url, headers=HEADERS)
        response.raise_for_status()
        print(f"Lease {lease_id} removido")

    print("Finalizado.")

if __name__ == "__main__":
    delete_leases()
