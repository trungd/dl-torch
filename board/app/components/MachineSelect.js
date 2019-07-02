// @flow
import React, { Component } from 'react';
import { Select, Button } from 'antd';
import {connect} from "react-redux";
import type {Machine} from "../reducers/types";
const { Option, OptGroup } = Select;

type Props = {
  machines: [Machine],
  value: any,
  handleChange: (machine: string) => void
};

class MachineSelect extends Component<Props> {
  onSelect = (keys, event) => {
    console.log('Trigger Select', keys, event);
  };

  onExpand = () => {
    console.log('Trigger Expand');
  };

  handleChange = () => {
    this.props.handleChange()
  };

  render() {
    return (
      <Select defaultValue="this" value={this.props.value} style={{ width: 300 }} onChange={this.handleChange}>
        {Object.entries(this.props.machines).map(([key, machine]) => (
          <Option key={key} value={key}>{machine.title} ({machine.host})</Option>
        ))}
        <OptGroup label="Others">
          <Option value="this">This Computer</Option>
          <Option value="add">Add Machine...</Option>
        </OptGroup>
      </Select>
    );
  }
}

function mapStateToProps(state) {
  console.log(state.settings.machines)
  return {
    machines: state.settings.machines
  }
}

export default connect(
  mapStateToProps,
  null
)(MachineSelect);