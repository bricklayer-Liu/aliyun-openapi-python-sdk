# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class MetastoreUpdateKafkaTopicRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'MetastoreUpdateKafkaTopic')

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_TopicId(self):
		return self.get_query_params().get('TopicId')

	def set_TopicId(self,TopicId):
		self.add_query_param('TopicId',TopicId)

	def get_TopicName(self):
		return self.get_query_params().get('TopicName')

	def set_TopicName(self,TopicName):
		self.add_query_param('TopicName',TopicName)

	def get_AdvancedConfig(self):
		return self.get_query_params().get('AdvancedConfig')

	def set_AdvancedConfig(self,AdvancedConfig):
		self.add_query_param('AdvancedConfig',AdvancedConfig)

	def get_NumPartitions(self):
		return self.get_query_params().get('NumPartitions')

	def set_NumPartitions(self,NumPartitions):
		self.add_query_param('NumPartitions',NumPartitions)

	def get_ReplicationFactor(self):
		return self.get_query_params().get('ReplicationFactor')

	def set_ReplicationFactor(self,ReplicationFactor):
		self.add_query_param('ReplicationFactor',ReplicationFactor)