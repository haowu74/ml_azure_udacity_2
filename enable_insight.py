from azureml.core import Workspace
from azureml.core.webservice import Webservice
from azureml.core.authentication import ServicePrincipalAuthentication
sdk_auth = ServicePrincipalAuthentication(tenant_id="425a5546-5a6e-4f1b-ab62-23d91d07d893",
                                          service_principal_id="8d78f2f0-26b9-4ab5-bb68-9ba4016aec1d",
                                          service_principal_password="T8gSjsU.s~QWCKAs.1F-CQLZ9l0Mg.xt32")
ws = Workspace(subscription_id="4a670da7-6d23-426f-a13b-c193c3c38be9",
               resource_group="MachineLearningResourceGroup",
               workspace_name="udacity-project",
               auth=sdk_auth
               )
aks_service= Webservice(workspace=ws, name="udacity-azureml-2-best-model")
aks_service.update(enable_app_insights=True)